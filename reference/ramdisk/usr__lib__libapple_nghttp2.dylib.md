# `/usr/lib/libapple_nghttp2.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 208,640 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 1696)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (2)

- `/usr/lib/libapple_nghttp2.dylib (compatibility version 1.0.0, current version 1.69.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (318)

```
HTTP_1_1_REQUIRED
Invalid stream state
nghttp2_stream_resume_deferred_item
content-disposition
Invalid state
nghttp2_stream.c
:scheme
http
nghttp2_rcbuf_decref
SETTINGS: unexpected ACK
Remote peer returned unexpected data while we expected SETTINGS frame.  Perhaps, peer does not support HTTP/2 properly.
i < iframe->niv
Protocol error
nghttp2_buf_avail(buf) >= 2 + altsvc->origin_len + altsvc->field_value_len
The current session is closing
ringbuf->len > 0
expires
sfparse_parser_param
request HEADERS: max concurrent streams exceeded
frame->hd.type == NGHTTP2_HEADERS
delta >= 0
Invalid frame octets
Stream was already closed or invalid
access-control-allow-origin
200
sfparse.c
nghttp2_submit_origin
nghttp2_session_mem_send2
request HEADERS: depend on itself
Ignoring received invalid HTTP header field: frame type: %u, stream: %d, name: [%.*s], value: [%.*s]
nghttp2_buf_avail(buf) >= 4 + priority_update->field_value_len
pq->q[item->index] == item
parser_string
stream->item
cookie
session->remote_window_size > 0
Callback was paused by the application
https
The transmission is not allowed for this stream
Flow control error
nghttp2_stream_defer_item
accept-language
age
nghttp2_submit.c
stream->state == NGHTTP2_STREAM_IDLE
RST_STREAM: stream_id == 0
GOAWAY: stream_id != 0
Server push is disabled by peer
nghttp2_frame_pack_ping
nghttp2_pq.c
SETTINGS: server attempted to enable push
SETTINGS: invalid SETTINGS_MAX_FRAME_SIZE
nghttp2_session_upgrade
stream->queued == 1
cache-control
buf->pos == buf->last
Invalid HTTP header field was received: frame type: %u, stream: %d, name: [%.*s], value: [%.*s]
Unknown error code
unknown
nghttp2_rcbuf.c
SETTINGS: invalid SETTINGS_ENBLE_PUSH
GOAWAY: invalid last_stream_id
nghttp2_session_upgrade2
session_ob_data_push
Cancel
transfer-encoding
sfparse_parser_dict
DATA: stream closed
EOF
nghttp2_hd.c
session_prep_frame
max-forwards
HEADERS: stream_id == 0
nghttp2_buf_avail(&iframe->lbuf) > 0
stream
nghttp2_session_mem_send_internal
DATA: stream_id == 0
nghttp2_helper.c
nghttp2_stream_attach_item
:path
session_pack_extension
SETTINGS_TIMEOUT
nghttp2_frame_unpack_priority_update_payload
nghttp2_frame_pack_window_update
server
SETTINGS: ACK and payload != 0
nghttp2_session_pack_data
nghttp2_session_get_local_settings
NO_ERROR
nghttp2_hd_table_get
SETTINGS: server attempted to disable SETTINGS_ENABLE_CONNECT_PROTOCOL
unexpected non-CONTINUATION frame or stream_id is invalid
DATA: invalid padding
session_after_header_block_received
PROTOCOL_ERROR
content-range
refresh
nghttp2_is_fatal(rv)
SETTINGS: stream_id != 0
nghttp2_session_set_stream_user_data
parser_dispstring
nghttp2_outbound_item_free
Too many inflight SETTINGS
'\"' == *sfp->pos
HEADERS: stream closed
inlen == 0
SETTINGS frame contained more than the maximum allowed entries
allow
expect
session->server
DATA: stream in reserved
session_process_settings_frame
nghttp2_buf_avail(buf) >= 4
:status
accept-encoding
FRAME_SIZE_ERROR
404
content-language
PRIORITY_UPDATE: max concurrent streams exceeded
Operation would block
Data transfer deferred
content-type
!parser_eof(sfp)
'%' == *sfp->pos
Success
When a local endpoint expects to receive SETTINGS frame, it receives an other type of frame
Received bad client magic byte string
host
parser_byteseq
RST_STREAM: stream in idle
Unsupported SPDY version
idx < ringbuf->len
(size_t)(p - (uint8_t *)ov_copy) == nov * sizeof(nghttp2_origin_entry) + len + nov
nghttp2_session_on_response_headers_received
SETTINGS: too large SETTINGS_INITIAL_WINDOW_SIZE
nghttp2_session_mem_recv2
SETTINGS expected
Stream is closing
content-length
content-location
if-match
link
referer
PUSH_PROMISE: invalid padding
session->obq_flood_counter_ > 0
session_end_stream_headers_received
idx >= 0
(stream->flags & NGHTTP2_STREAM_FLAG_DEFERRED_ALL) == 0
hd_ringbuf_get
gzip, deflate
push response HEADERS: stream_id == 0
DATA: stream not opened
Stream ID is invalid
Violation in HTTP messaging rule
:method
rcbuf->ref > 0
initial_state != NGHTTP2_STREAM_IDLE
PUSH_PROMISE: push disabled
request HEADERS is not allowed
GOAWAY has already been sent
STREAM_CLOSED
POST
too large frame size
DATA: insufficient padding space
bufs->head == bufs->cur
Another DATA frame has already been deferred
Too many CONTINUATION frames following a HEADER frame
nghttp2_buf_avail(buf) >= NGHTTP2_PRIORITY_SPECLEN
date
':' == *sfp->pos
PRIORITY_UPDATE: prioritizing idle push is not allowed
The user callback function failed
FLOW_CONTROL_ERROR
nghttp2_map.c
400
500
nghttp2_session_add_settings
INTERNAL_ERROR
sfparse_parser_inner_list
nghttp2_frame_pack_settings
nghttp2_frame_pack_origin
/
etag
nghttp2_outbound_item.c
stream->item == item
Invalid argument
accept
PRIORITY_UPDATE is received from server
session_close_stream_on_goaway
rv == 0
No more Stream ID available
REFUSED_STREAM
INDEX_RANGE_VALID(context, idx)
1.69.0
HEADERS: insufficient padding space
nghttp2_buf_len(buf) == NGHTTP2_FRAME_HDLEN + frame->hd.length
/index.html
content-encoding
from
location
nghttp2_buf_avail(buf) >= datamax
session->last_sent_stream_id + 2 <= frame->push_promise.promised_stream_id
WINDOW_UPADATE to reserved stream
nghttp2_frame_pack_priority_update
payloadlen >= 4
accept-charset
proclen == readlen
via
nghttp2_submit_data2
PING: stream_id != 0
nghttp2_session_recv
find_stream_on_goaway_func
DATA or HEADERS frame has already been submitted for the stream
Invalid HTTP header field was received
nghttp2_frame_pack_headers
user-agent
parser_number
stream->closed_next == NULL
DATA: stream in idle
0 == rv
The user callback function failed due to the temporal error
CONNECT_ERROR
nghttp2_frame_pack_rst_stream
'@' == *sfp->pos
nghttp2_session.c
push response HEADERS: max concurrent streams exceeded
SETTINGS: invalid SETTINGS_ENABLE_CONNECT_PROTOCOL
session_ob_data_remove
INADEQUATE_SECURITY
nghttp2_frame_pack_goaway
last-modified
www-authenticate
request HEADERS: invalid stream_id
if-modified-since
set-cookie
DATA: stream in half-closed(remote)
Flooding was detected in this HTTP/2 session, and it must be closed
COMPRESSION_ERROR
if-unmodified-since
'?' == *sfp->pos
nghttp2_submit_data
SETTINGS: SETTINGS_NO_RFC7540_PRIORITIES cannot be changed
session_after_frame_sent1
!session->server
Out of buffer space
Out of memory
GET
proxy-authenticate
data_prd
nghttp2_session_open_stream
stream->state == NGHTTP2_STREAM_OPENING && nghttp2_session_is_my_stream_id(session, frame->hd.stream_id)
nghttp2_increase_local_window_size
The length of the frame is invalid
Stream was refused
map_resize
trailers
nghttp2_session_on_push_response_headers_received
urgency < NGHTTP2_EXTPRI_URGENCY_LEVELS
Internal error
206
accept-ranges
h2
session->callbacks.pack_extension_callback2 || session->callbacks.pack_extension_callback
HEADERS: no HEADERS allowed from client in reserved state
SETTINGS: invalid SETTINGS_NO_RFC7540_PRIORITIES
PUSH_PROMISE: stream_id == 0
range
nghttp2_frame_pack_altsvc
nghttp2_pq_remove
stream->state == NGHTTP2_STREAM_RESERVED
retry-after
vary
nghttp2_session_on_priority_update_received
PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n
nghttp2_buf_avail(buf) >= 8
204
PUSH_PROMISE: stream in idle
PUSH_PROMISE: stream closed
PRIORITY_UPDATE: stream_id == 0
headers_frame->hd.type == NGHTTP2_HEADERS
WINDOW_UPDATE: window_size_increment == 0
hd_ringbuf_pop_back
304
if-range
stream->queued == 0
nghttp2_frame_pack_push_promise
if-none-match
PUSH_PROMISE: invalid promised_stream_id
SETTINGS: too many setting entries
session->last_sent_stream_id < frame->hd.stream_id
CANCEL
request HEADERS: client received request
Insufficient buffer size given to function
nghttp2_frame.c
authorization
CONTINUATION: unexpected
nghttp2_session_get_remote_settings
nghttp2_frame_add_pad
strict-transport-security
parser_boolean
HEADERS: invalid padding
iframe->state == NGHTTP2_IB_IGN_ALL
WINDOW_UPDATE: window size overflow
session_sched_reschedule_stream
nghttp2_buf_avail(buf) >= padlen - 1
:authority
proxy-authorization
parser_date
PUSH_PROMISE: invalid stream_id
Invalid header block
Header compression/decompression error
ENHANCE_YOUR_CALM
nghttp2_frame_pack_priority
nghttp2_session_add_rst_stream_continue
request HEADERS: stream_id == 0
PUSH_PROMISE: insufficient padding space
0
WINDOW_UPDATE to idle stream
```
