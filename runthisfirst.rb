# Run this before you run the tweetmytheremin python code

live_loop :listen do
  use_real_time
  note = sync "/osc/play_this"
  puts note
  play note
end