package io.fsq.twofishes.indexer.output

import com.mongodb.Bytes
import com.mongodb.casbah.Imports._
import io.fsq.twofishes.indexer.mongo.MongoGeocodeDAO
import io.fsq.twofishes.util.{DurationUtils, StoredFeatureId}
import java.io._
import org.apache.hadoop.hbase.util.Bytes._
import salat._
import salat.annotations._
import salat.dao._
import salat.global._
import scala.collection.JavaConverters._
import scala.collection.mutable.HashMap

class FidMap(preload: Boolean) extends DurationUtils {
  val fidMap = new HashMap[StoredFeatureId, Option[StoredFeatureId]]

  if (preload) {
    logPhase("preloading fids") {
      var i = 0
      val total = MongoGeocodeDAO.collection.count()
      val geocodeCursor = MongoGeocodeDAO.find(MongoDBObject())
      geocodeCursor.option = Bytes.QUERYOPTION_NOTIMEOUT
      geocodeCursor.foreach(geocodeRecord => {
        geocodeRecord.featureIds.foreach(id => {
          fidMap(id) = Some(geocodeRecord.featureId)
        })
        i += 1
        if (i % (100*1000) == 0) {
          log.info("preloaded %d/%d fids".format(i, total))
        }
      })
    }
  }

  def get(fid: StoredFeatureId): Option[StoredFeatureId] = {
    if (preload) {
      fidMap.getOrElse(fid, None)
    } else {
      if (!fidMap.contains(fid)) {
        val longidOpt = MongoGeocodeDAO.primitiveProjection[Long](
          MongoDBObject("_id" -> fid.longId), "_id")
        fidMap(fid) = longidOpt.flatMap(StoredFeatureId.fromLong _)
        if (longidOpt.isEmpty) {
          //println("missing fid: %s".format(fid))
        }
      }

      fidMap.getOrElseUpdate(fid, None)
    }
  }
}
