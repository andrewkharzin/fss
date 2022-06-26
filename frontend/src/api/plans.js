import { HTTP } from './common'
export const Plan = {
//   create (config) {
//     return HTTP.post('/plans/', config).then(response => {
//       return response.data
//     })
//   },
//   delete (note) {
//     return HTTP.delete(`/notes/${note.id}/`)
//   },
  list () {
    return HTTP.get('/plans/').then(response => {
      return response.data
    })
  }
}
