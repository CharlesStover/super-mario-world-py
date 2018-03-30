from datetime import datetime
from mario import mario

Model = {
  'lastRender': datetime.now(),
  'objects': [ mario ],
  'renders': 0,
  'scrollX': 0,
  'scrollY': 0
}
