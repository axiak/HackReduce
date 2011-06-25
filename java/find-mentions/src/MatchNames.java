import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;



public class MatchNames extends Configured implements Tool {
  public static final String INPUT_PATH = "/datasets/ngrams/";
	public static final String OUTPUT_PATH = "/mnt/team6/bpopp/out";
	
	@Override
	public int run(String[] arg0) throws Exception {
			
		Configuration conf = getConf();
	
		FileSystem hdfs = FileSystem.get(conf);
		hdfs.delete(new Path(OUTPUT_PATH), true);
		
		Job job = new Job(conf, "match-names");
		job.setJarByClass(MatchNames.class);

		job.setMapperClass(MatchNamesMapper.class);
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);
		
		FileOutputFormat.setOutputPath(job, new Path(OUTPUT_PATH));
		FileInputFormat.addInputPath(job, new Path(INPUT_PATH + "1gram"));
		FileInputFormat.addInputPath(job, new Path(INPUT_PATH + "2gram"));
		
		return job.waitForCompletion(true) ? 0 : 1;		
	}
	
	
    public static void main(String[] args) throws Exception {
        // Let ToolRunner handle generic command-line options 
        int res = ToolRunner.run(new Configuration(), new MatchNames(), args);
        
        System.exit(res);
      }
}
