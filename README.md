# Assault Website Load Generator

This package will allow a user to generate http traffic to their website.  It will allow for specifying number of requests to make (-r) and if we want to test concurrency (-c) for concurrent users.

## Example

`assault -r 3000 -c 10 http://example.com `

.... Done!

-- Results -- | --Values--
----------------|------------------
Successful requests | 3000
Slowest|0.010s
Fastest | 0.001s
Average | 0.003s
Total time | 2.400s
Requests per min | 90000
Requests per sec | 1250 
...

If you'd like to see these results in JSON format, you can use the **-j** flag with a path to a JSON file. :rocket:

...



