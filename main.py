from mapreduce import mapreduce_pipeline
import webapp2
import logging
import collections 

#recv input readers data return key value tuple generator
def mapper(entity):
    result = collections.Counter(entity.link)
    for key, value in result.items():
        yield key, value
    

#recv mapper result merge (key, values)
def reduce(key, values):
    total = sum(values)
    logging.info("{}:{}".format(key, total))
    yield key, total


class Execute_Mapreduce(webapp2.RequestHandler):
    def get(self):
        pipeline = mapreduce_pipeline.MapreducePipeline(
            "test",
            "main.mapper",
            "main.reduce",
            "mapreduce.input_readers.DatastoreInputReader",
            "mapreduce.output_writers.BlobstoreOutputWriter",
            mapper_params={
                "input_reader": {
                    "entity_kind": "models.ProductItem",
                    "batch_size": 50,
                },
            },
            reducer_params={
                "mime_type": "text/plain",
            },
            shards=16
        )
        pipeline.start()
        self.redirect(pipeline.base_path + "/status?root=" + pipeline.pipeline_id) #pipeline console


app = webapp2.WSGIApplication([
    (r'/execute_mapreduce', Execute_Mapreduce),
])
