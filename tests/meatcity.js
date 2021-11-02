import { sleep } from 'k6'
import http from 'k6/http'

// See https://k6.io/docs/using-k6/options
export const options = {
  stages: [
    { duration: '30s', target: 1 },
    { duration: '30s', target: 5 },
    { duration: '30s', target: 10 },
    { duration: '30s', target: 25 },
    { duration: '30s', target: 50 },
    { duration: '30s', target: 75 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.02'], // http errors should be less than 2%
    http_req_duration: ['p(95)<2000'], // 95% requests should be below 2s
  },
  ext: {
    loadimpact: {
      distribution: {
        'amazon:us:ashburn': { loadZone: 'amazon:us:ashburn', percent: 100 },
      },
      apm: [
        {
          provider: "prometheus",
          remoteWriteURL: "https://cortex.safemoon.joshcorp.co/api/prom/push",
          // optional parameters
          includeDefaultMetrics: true,
          metrics: ["http_req_sending", "http_req_duration", "http_reqs", "vus", "checks"],
          includeTestRunId: true,
          resampleRate: 3
        },
      ]
    },
  },
}

export default function main() {
  let response = http.get('https://climeat-api.safemoon.joshcorp.co/cities/Moscow')
  sleep(1)
}