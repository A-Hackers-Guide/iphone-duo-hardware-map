# `/usr/lib/libapple_nghttp2.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 208,640 bytes.

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
When a local endpoint expects to receive SETTINGS frame, it receives an other type of frame
GOAWAY: stream_id != 0
nghttp2_session_mem_recv2
nghttp2_frame_unpack_priority_update_payload
access-control-allow-origin
proxy-authenticate
nghttp2_submit_data
SETTINGS: invalid SETTINGS_ENABLE_CONNECT_PROTOCOL
session->last_sent_stream_id + 2 <= frame->push_promise.promised_stream_id
The length of the frame is invalid
Flow control error
sfparse_parser_param
rv == 0
content-encoding
nghttp2_rcbuf.c
initial_state != NGHTTP2_STREAM_IDLE
if-modified-since
GOAWAY: invalid last_stream_id
session_process_settings_frame
Too many CONTINUATION frames following a HEADER frame
accept-encoding
content-length
range
PUSH_PROMISE: stream_id == 0
PUSH_PROMISE: push disabled
Invalid state
allow
nghttp2_submit.c
SETTINGS: server attempted to enable push
0
WINDOW_UPDATE: window size overflow
nghttp2_increase_local_window_size
SETTINGS frame contained more than the maximum allowed entries
refresh
nghttp2_buf_avail(&iframe->lbuf) > 0
Ignoring received invalid HTTP header field: frame type: %u, stream: %d, name: [%.*s], value: [%.*s]
200
HEADERS: stream_id == 0
Stream was refused
h2
(size_t)(p - (uint8_t *)ov_copy) == nov * sizeof(nghttp2_origin_entry) + len + nov
SETTINGS: too large SETTINGS_INITIAL_WINDOW_SIZE
session->server
PRIORITY_UPDATE is received from server
i < iframe->niv
Unsupported SPDY version
STREAM_CLOSED
nghttp2_buf_len(buf) == NGHTTP2_FRAME_HDLEN + frame->hd.length
idx < ringbuf->len
accept
user-agent
push response HEADERS: max concurrent streams exceeded
RST_STREAM: stream_id == 0
The user callback function failed
NO_ERROR
nghttp2_frame_pack_priority_update
hd_ringbuf_pop_back
Received bad client magic byte string
INADEQUATE_SECURITY
400
parser_dispstring
SETTINGS: invalid SETTINGS_NO_RFC7540_PRIORITIES
HEADERS: insufficient padding space
nghttp2_map.c
SETTINGS: unexpected ACK
session->last_sent_stream_id < frame->hd.stream_id
session_end_stream_headers_received
:authority
!parser_eof(sfp)
http
Stream is closing
Invalid HTTP header field was received
unknown
accept-ranges
inlen == 0
stream
nghttp2_helper.c
nghttp2_buf_avail(buf) >= 8
:scheme
https
Out of memory
FRAME_SIZE_ERROR
nghttp2_frame_pack_headers
parser_number
Invalid frame octets
The user callback function failed due to the temporal error
nghttp2_frame_add_pad
nghttp2_hd_table_get
server
vary
stream->item == item
session_close_stream_on_goaway
PRIORITY_UPDATE: max concurrent streams exceeded
location
nghttp2_session_add_rst_stream_continue
too large frame size
CONTINUATION: unexpected
session->callbacks.pack_extension_callback2 || session->callbacks.pack_extension_callback
EOF
:status
nghttp2_is_fatal(rv)
session_pack_extension
No more Stream ID available
Another DATA frame has already been deferred
HTTP_1_1_REQUIRED
nghttp2_buf_avail(buf) >= 4
nghttp2_frame_pack_window_update
nghttp2_hd.c
if-match
bufs->head == bufs->cur
buf->pos == buf->last
nghttp2_buf_avail(buf) >= NGHTTP2_PRIORITY_SPECLEN
nghttp2_session_upgrade
session_after_frame_sent1
if-unmodified-since
transfer-encoding
nghttp2_session_mem_send2
stream->state == NGHTTP2_STREAM_RESERVED
SETTINGS: server attempted to disable SETTINGS_ENABLE_CONNECT_PROTOCOL
frame->hd.type == NGHTTP2_HEADERS
session_prep_frame
content-type
rcbuf->ref > 0
nghttp2_session_on_response_headers_received
push response HEADERS: stream_id == 0
nghttp2_frame_pack_ping
accept-charset
proxy-authorization
sfparse.c
':' == *sfp->pos
SETTINGS: SETTINGS_NO_RFC7540_PRIORITIES cannot be changed
session_sched_reschedule_stream
nghttp2_buf_avail(buf) >= 4 + priority_update->field_value_len
content-disposition
'\"' == *sfp->pos
PUSH_PROMISE: insufficient padding space
nghttp2_session_pack_data
age
parser_boolean
PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n
Remote peer returned unexpected data while we expected SETTINGS frame.  Perhaps, peer does not support HTTP/2 properly.
WINDOW_UPDATE: window_size_increment == 0
nghttp2_frame_pack_goaway
expect
www-authenticate
CANCEL
'@' == *sfp->pos
DATA: stream closed
Stream ID is invalid
PROTOCOL_ERROR
nghttp2_buf_avail(buf) >= 2 + altsvc->origin_len + altsvc->field_value_len
hd_ringbuf_get
set-cookie
via
nghttp2_frame_pack_altsvc
nghttp2_submit_origin
stream->closed_next == NULL
DATA: stream in half-closed(remote)
Internal error
nghttp2_pq.c
0 == rv
delta >= 0
Invalid header block
etag
nghttp2_outbound_item_free
request HEADERS: depend on itself
nghttp2_session_recv
stream->item
if-range
max-forwards
parser_string
1.69.0
stream->queued == 1
FLOW_CONTROL_ERROR
nghttp2_frame.c
304
Protocol error
nghttp2_stream_resume_deferred_item
nghttp2_buf_avail(buf) >= padlen - 1
INDEX_RANGE_VALID(context, idx)
gzip, deflate
PING: stream_id != 0
request HEADERS is not allowed
Callback was paused by the application
SETTINGS_TIMEOUT
parser_date
parser_byteseq
unexpected non-CONTINUATION frame or stream_id is invalid
DATA or HEADERS frame has already been submitted for the stream
nghttp2_frame_pack_rst_stream
204
accept-language
pq->q[item->index] == item
SETTINGS: ACK and payload != 0
SETTINGS expected
!session->server
date
last-modified
'?' == *sfp->pos
data_prd
SETTINGS: invalid SETTINGS_MAX_FRAME_SIZE
PUSH_PROMISE: stream closed
SETTINGS: too many setting entries
DATA: stream_id == 0
request HEADERS: stream_id == 0
nghttp2_session_on_push_response_headers_received
Success
Insufficient buffer size given to function
Violation in HTTP messaging rule
nghttp2_frame_pack_push_promise
nghttp2_frame_pack_origin
host
nghttp2_submit_data2
WINDOW_UPADATE to reserved stream
authorization
from
retry-after
'%' == *sfp->pos
POST
sfparse_parser_inner_list
proclen == readlen
The current session is closing
INTERNAL_ERROR
206
404
nghttp2_session.c
PRIORITY_UPDATE: prioritizing idle push is not allowed
nghttp2_buf_avail(buf) >= datamax
Invalid HTTP header field was received: frame type: %u, stream: %d, name: [%.*s], value: [%.*s]
Server push is disabled by peer
content-location
nghttp2_outbound_item.c
session->obq_flood_counter_ > 0
map_resize
nghttp2_stream_defer_item
HEADERS: stream closed
SETTINGS: stream_id != 0
PUSH_PROMISE: invalid stream_id
nghttp2_session_get_remote_settings
nghttp2_session_upgrade2
CONNECT_ERROR
strict-transport-security
HEADERS: no HEADERS allowed from client in reserved state
PRIORITY_UPDATE: stream_id == 0
nghttp2_session_set_stream_user_data
idx >= 0
headers_frame->hd.type == NGHTTP2_HEADERS
request HEADERS: client received request
request HEADERS: invalid stream_id
request HEADERS: max concurrent streams exceeded
nghttp2_session_mem_send_internal
Invalid stream state
GOAWAY has already been sent
:path
/
content-language
expires
referer
sfparse_parser_dict
PUSH_PROMISE: invalid padding
nghttp2_session_get_local_settings
Too many inflight SETTINGS
Flooding was detected in this HTTP/2 session, and it must be closed
COMPRESSION_ERROR
nghttp2_frame_pack_settings
/index.html
500
Header compression/decompression error
Unknown error code
nghttp2_frame_pack_priority
payloadlen >= 4
stream->state == NGHTTP2_STREAM_OPENING && nghttp2_session_is_my_stream_id(session, frame->hd.stream_id)
SETTINGS: invalid SETTINGS_ENBLE_PUSH
PUSH_PROMISE: invalid promised_stream_id
DATA: insufficient padding space
DATA: invalid padding
find_stream_on_goaway_func
cache-control
if-none-match
nghttp2_rcbuf_decref
nghttp2_session_open_stream
DATA: stream in idle
The transmission is not allowed for this stream
REFUSED_STREAM
ENHANCE_YOUR_CALM
nghttp2_stream.c
ringbuf->len > 0
stream->queued == 0
session->remote_window_size > 0
Operation would block
Data transfer deferred
stream->state == NGHTTP2_STREAM_IDLE
WINDOW_UPDATE to idle stream
session_after_header_block_received
Out of buffer space
nghttp2_stream_attach_item
content-range
urgency < NGHTTP2_EXTPRI_URGENCY_LEVELS
session_ob_data_remove
Stream was already closed or invalid
(stream->flags & NGHTTP2_STREAM_FLAG_DEFERRED_ALL) == 0
HEADERS: invalid padding
iframe->state == NGHTTP2_IB_IGN_ALL
nghttp2_session_add_settings
Cancel
session_ob_data_push
GET
nghttp2_pq_remove
trailers
nghttp2_session_on_priority_update_received
DATA: stream in reserved
Invalid argument
:method
RST_STREAM: stream in idle
DATA: stream not opened
cookie
link
PUSH_PROMISE: stream in idle
```
