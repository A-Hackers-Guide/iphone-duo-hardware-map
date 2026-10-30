# `/usr/lib/system/libsystem_symptoms.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 146,544 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 30 (Size: 2520)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (12)

- `/usr/lib/system/libsystem_symptoms.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0, upward)`
- `/usr/lib/system/libmacho.dylib (compatibility version 1.0.0, current version 1040.0.0)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.2)`

## Entitlements

```xml
  - no entitlements
```

## Strings (185)

```
 sb_timestamp_secs  %d\n
srs_ack_id              %0x\n
connection error: %s\n
send_current: ack_id %d\n
 sb_qualifier[%d]    %llx\n
 drop (NOMEM)
connection handler received object  %p
handling incoming message
filter_new_symptom: too old DROP
reset_sr_filters for %s\n
reevaluate_sc_symptoms: sc was active, dequeued\n
connect_symptom_framework: exit
actionable new fallback disposition: (dispo/grant/hinted): %d/%llu/%llu
symptoms_transport_dropped %s, immediate reconnect, but connect queued\n
 sb_flags           %x\n
    cf_queue_len_max    %x\n
 sc_id                  %x\n
payload
reevaluate_sc_symptoms: after evaluate symptom\n
find_symptom_reporter_by_name  returns NULL\n
create_symptom_framework returns %p, name %s\n
    cf_filter_seqno     %x\n
Drop (immediate)
read_symptoms for sc %p, q len %zu\n
filter_new_symptom: DROP_HEAD (Age limit)
   s_magic      %x\n
type
handle_incoming_xpc_dictionary:  ERR message with no payload
+++ SYMPTOMSD MESSAGE RECEIVED +++\n
read_symptoms_from_q: no next symptom available
transport OK
ensure_symptom_framework_connect: connect after delay\n
connect_symptom_framework: ensure_alert\n
 EAGAIN !!!
symptom_post action flags %x from filter %p\n
filter_new_symptom: return %x\n
%s symptoms
connect_symptom_framework: exit\n
connect_symptom_framework: ensure_alert
 sr_ctrl_head        first, last  %p %p\n
 alert
error
SymptomReporter: XPC connection to Symptom Framework interrupted\n
symptom_transport: unhandled connection error: %s
handle_symptom: filter with global filter\n
symptom_ctrl at %p\n
 sr_q_counts         %lu\n
dump_active_idents.. 
System global... 
com.apple.WebKit.Networking
symptom_transport_send:  ERR no dictionary
SymptomReporter incoming_message, SYMTLV_FILTER sz %zd fails consistency checks, desc->stlv_len %d
handle_symptom: filter with sc filter\n
 sb_timestamp_nsecs %d\n
 sc_active_link         %p\n
filter_new_symptom: entry, q->sq_len %lu cf->cf_queue_len_max %d cf->cf_queue_len_alert %d\n
filter_new_symptom: cf->cf_queue_len_max == 0, DROP
apply_new_filters, Symptom: %x   Qlert %d    Q drop %d\n
Symptom ID %x    
 (note, dropped older)
 sr_filter ...
howmany
%s: %s
Free symptom %p, %s
srs_num_alerts          %d\n
srs_version             %d\n
srs_sym_basic   ...
symptom_transport_connect event handler called on %p for %p evcount %lu errcount %lu\n
Drop (filter)
ensure_symptom_framework_connect %s, set sr_connect_queued\n
handle_symptom: filter with sc filter
 Symptom at %p\n
 save
 reinit
filter_new_symptom: q->sq_len %zdd >= cf->cf_queue_len_alert %d ALERT\n
read_current_status, ack id %d, flags %d num_alerts %d  num_queued %d\n
reevaluate_sc_symptoms: evaluate symptom %p\n
filter_new_symptom: DROP_HEAD
QUAL[%d] %llx 
 ack-id %d  num-alerts %d num-queued %d
com.apple.symptoms.service.queue
filter_new_symptom: DROP_HEAD\n
ensure_connect, update backoff value, uptime_secs %lu\n
 ALERTS posted %d
 sb_ident           %d\n
 sc_symptom_q first, last %p %p\n
 alert-send
 sc_filter ...
dump_idents.. 
uuid
 sb_version         %d\n
srs_num_queued          %d\n
 sc_magic               %x\n
Reporter status:
handle_incoming_xpc_dictionary:  desc %p size %lu\n
symptom_post obtained control structure at %p\n
connect_symptom_framework called
 drop
Symptom Sender Name: %s
 sc_symptom_q len %lu\n
v8@?0
incorrect dict: %p
symptom_transport_send:  ptr %p size %lu \n
Singlethreaded
SymptomReporter incoming_message, SYMTLV_READ sz too small %zd
update globals to remove symptom at %p\n
Sent STATUS flags
srs_flags               %0x\n
 sr_ctrl_num    %lu\n
incorrect arguments (queue/completion): %p/%p
symptom_transport_send:  ERR no dictionary\n
symptom_post entry, symptom pointer %p\n
After sym_ctrl_dequeue  %p\n
read_symptoms_from_q: entry\n
 sent
event_data
failed to connect to %s\n
symptoms_transport_dropped %s, immediate reconnect\n
handle_symptom entry, symptom pointer %p   sc filter seqno %d  sr seqno %d\n
reevaluate_sr_symptoms: evaluate symptom control %p, id %x\n
+++ SYMPTOMSD MESSAGE RECEIVED +++
 sc_active_link_in_use  %d\n
Not Multithreaded
symptom_transport: XPC connection invalid for %s, switch to %s\n
symptom_transport: CONNECTION_INVALID
filter_new_symptom: DROP_HEAD (Age limit)\n
delay_after_interruption is %lld nanoseconds\n
connect_symptom_framework: %s transport connect failed, unset sr_connect_queued\n
connect_symptom_framework: %s transport connect OK, unset sr_connect_queued\n
   s_link next  %p\n
symptom_transport: CONNECTION_INVALID\n
apply_new_filters, count is %zd, seqno %d\n
<nil>
read_symptoms_from_q: entry
read_symptoms_from_q: added next symptom
 sc_flags               %x\n
 sc_link                %p\n
symptom_transport: skipping TERMINATION_IMMINENT event\n
symptom_transport: skipping TERMINATION_IMMINENT event
SymptomReporter incoming_message, SYMTLV_FILTER sc %zd desc->stlv_len %d filter size %zd
push_symptom_to_nhm, symptom %p\n
reevaluate_sc_symptoms: sr %p sc %p\n
find_symptom_reporter_by_name  returns NULL
ACTION:
 alert-pend
No mem
apply_new_filters
find_symptom_reporter_by_name  %s   len %ld\n
 sr_num_active  %lu\n
 resp
reason_code
symptom_transport_connect called, connecting to %s\n
SymptomReporter: Disabling Symptom Transport after perstent invalid connections\n
symptoms_transport_dropped %s\n
ensure_sym_ctrl_is_queued, sc %p, in use %d\n
update_filter_values, max age %d, alert len %d drop len %d seqno %d\n
 SYMPTOM-LOG-STRING: %s\n
com.apple.WebKit.WebContent
com.apple.symptoms.symptomsd.managed_events
Disabled
new_symptoms_read: ack_id %d\n
read_symptoms_from_q: added next symptom\n
symptom_init_queue
ensure_symptom_framework_connect: connect after delay
    cf_queue_len_alert  %x\n
 sr_filter_seqno  %u\n
seqno
 sr_ctrl_active_head first, last  %p %p\n
 sr_alert_sent       %d\n
unexpected message from peer %p
Too old
read_symptoms for sr %p %s\n
connect_symptom_framework called\n
incorrect event_data: %p
Queue length limit
find_symptom_reporter_by_name  check sr %p name len %ld\n
handle_symptom: filter with global filter
reevaluate_sc_symptoms: after evaluate symptom
v16@?0^v8
incorrect event_data count: %zu
com.apple.usymptomsd
SymptomReporter incoming_message, SYMTLV_TERMINAL_ACK sz too small %zd
After ensure_sym_ctrl_is_queued %p\n
reevaluate_sc_symptoms: sc was active, dequeued
Status Sender Name: %s
```
