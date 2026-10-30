# `/usr/lib/system/libsystem_symptoms.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 146,544 bytes.

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
 resp
symptom_transport_send:  ERR no dictionary\n
+++ SYMPTOMSD MESSAGE RECEIVED +++\n
SymptomReporter incoming_message, SYMTLV_TERMINAL_ACK sz too small %zd
symptom_post action flags %x from filter %p\n
apply_new_filters, Symptom: %x   Qlert %d    Q drop %d\n
 ack-id %d  num-alerts %d num-queued %d
 sb_timestamp_nsecs %d\n
 sc_link                %p\n
 sc_symptom_q first, last %p %p\n
symptom_post obtained control structure at %p\n
push_symptom_to_nhm, symptom %p\n
 sr_q_counts         %lu\n
find_symptom_reporter_by_name  %s   len %ld\n
connect_symptom_framework called
 sr_ctrl_active_head first, last  %p %p\n
Not Multithreaded
payload
Drop (immediate)
connect_symptom_framework: ensure_alert
 drop (NOMEM)
 alert
type
symptom_transport_connect event handler called on %p for %p evcount %lu errcount %lu\n
read_symptoms for sr %p %s\n
read_symptoms_from_q: added next symptom\n
connect_symptom_framework: ensure_alert\n
find_symptom_reporter_by_name  returns NULL
 sb_flags           %x\n
srs_num_alerts          %d\n
 sc_magic               %x\n
com.apple.WebKit.Networking
reason_code
failed to connect to %s\n
Too old
filter_new_symptom: DROP_HEAD (Age limit)
 sb_ident           %d\n
symptom_transport: XPC connection invalid for %s, switch to %s\n
handling incoming message
symptom_transport: skipping TERMINATION_IMMINENT event
 sc_active_link         %p\n
 sc_symptom_q len %lu\n
 sr_num_active  %lu\n
ACTION:
symptom_transport: unhandled connection error: %s
reevaluate_sc_symptoms: after evaluate symptom\n
uuid
incorrect dict: %p
read_symptoms for sc %p, q len %zu\n
connect_symptom_framework: exit
 EAGAIN !!!
    cf_filter_seqno     %x\n
dump_idents.. 
incorrect arguments (queue/completion): %p/%p
actionable new fallback disposition: (dispo/grant/hinted): %d/%llu/%llu
filter_new_symptom: q->sq_len %zdd >= cf->cf_queue_len_alert %d ALERT\n
read_symptoms_from_q: entry\n
reevaluate_sc_symptoms: sc was active, dequeued\n
 sb_version         %d\n
 sb_qualifier[%d]    %llx\n
srs_num_queued          %d\n
 sr_ctrl_head        first, last  %p %p\n
handle_symptom: filter with sc filter
srs_version             %d\n
srs_flags               %0x\n
srs_sym_basic   ...
incorrect event_data count: %zu
srs_ack_id              %0x\n
event_data
Disabled
symptoms_transport_dropped %s, immediate reconnect, but connect queued\n
new_symptoms_read: ack_id %d\n
Symptom Sender Name: %s
 (note, dropped older)
com.apple.WebKit.WebContent
symptom_transport: skipping TERMINATION_IMMINENT event\n
handle_symptom: filter with global filter\n
connect_symptom_framework: exit\n
<nil>
    cf_queue_len_alert  %x\n
symptom_transport: CONNECTION_INVALID\n
com.apple.usymptomsd
Singlethreaded
SymptomReporter incoming_message, SYMTLV_READ sz too small %zd
filter_new_symptom: entry, q->sq_len %lu cf->cf_queue_len_max %d cf->cf_queue_len_alert %d\n
Queue length limit
apply_new_filters, count is %zd, seqno %d\n
 sc_filter ...
v8@?0
%s: %s
Free symptom %p, %s
symptoms_transport_dropped %s\n
transport OK
ensure_connect, update backoff value, uptime_secs %lu\n
ensure_symptom_framework_connect: connect after delay\n
 ALERTS posted %d
handle_symptom: filter with sc filter\n
connect_symptom_framework called\n
    cf_queue_len_max    %x\n
 sc_flags               %x\n
symptom_transport_send:  ERR no dictionary
SymptomReporter incoming_message, SYMTLV_FILTER sz %zd fails consistency checks, desc->stlv_len %d
filter_new_symptom: DROP_HEAD\n
delay_after_interruption is %lld nanoseconds\n
symptom_init_queue
reevaluate_sc_symptoms: sc was active, dequeued
 sb_timestamp_secs  %d\n
 sr_alert_sent       %d\n
error
connection handler received object  %p
handle_incoming_xpc_dictionary:  desc %p size %lu\n
filter_new_symptom: cf->cf_queue_len_max == 0, DROP
filter_new_symptom: return %x\n
reset_sr_filters for %s\n
incorrect event_data: %p
connection error: %s\n
handle_symptom entry, symptom pointer %p   sc filter seqno %d  sr seqno %d\n
read_symptoms_from_q: no next symptom available
send_current: ack_id %d\n
SymptomReporter: Disabling Symptom Transport after perstent invalid connections\n
SymptomReporter incoming_message, SYMTLV_FILTER sc %zd desc->stlv_len %d filter size %zd
QUAL[%d] %llx 
   s_link next  %p\n
seqno
SymptomReporter: XPC connection to Symptom Framework interrupted\n
reevaluate_sc_symptoms: sr %p sc %p\n
create_symptom_framework returns %p, name %s\n
Symptom ID %x    
symptom_ctrl at %p\n
dump_active_idents.. 
After ensure_sym_ctrl_is_queued %p\n
Status Sender Name: %s
 sc_active_link_in_use  %d\n
 sr_ctrl_num    %lu\n
 sent
v16@?0^v8
com.apple.symptoms.service.queue
update globals to remove symptom at %p\n
update_filter_values, max age %d, alert len %d drop len %d seqno %d\n
symptom_post entry, symptom pointer %p\n
read_current_status, ack id %d, flags %d num_alerts %d  num_queued %d\n
ensure_symptom_framework_connect %s, set sr_connect_queued\n
connect_symptom_framework: %s transport connect failed, unset sr_connect_queued\n
ensure_symptom_framework_connect: connect after delay
unexpected message from peer %p
symptoms_transport_dropped %s, immediate reconnect\n
filter_new_symptom: DROP_HEAD (Age limit)\n
apply_new_filters
%s symptoms
Reporter status:
Sent STATUS flags
 drop
Drop (filter)
connect_symptom_framework: %s transport connect OK, unset sr_connect_queued\n
read_symptoms_from_q: added next symptom
 Symptom at %p\n
   s_magic      %x\n
com.apple.symptoms.symptomsd.managed_events
howmany
filter_new_symptom: DROP_HEAD
 save
 alert-send
No mem
reevaluate_sc_symptoms: evaluate symptom %p\n
find_symptom_reporter_by_name  returns NULL\n
 sr_filter_seqno  %u\n
 alert-pend
 reinit
handle_incoming_xpc_dictionary:  ERR message with no payload
symptom_transport: CONNECTION_INVALID
filter_new_symptom: too old DROP
After sym_ctrl_dequeue  %p\n
find_symptom_reporter_by_name  check sr %p name len %ld\n
 sr_filter ...
symptom_transport_send:  ptr %p size %lu \n
ensure_sym_ctrl_is_queued, sc %p, in use %d\n
reevaluate_sr_symptoms: evaluate symptom control %p, id %x\n
handle_symptom: filter with global filter
reevaluate_sc_symptoms: after evaluate symptom
 SYMPTOM-LOG-STRING: %s\n
System global... 
symptom_transport_connect called, connecting to %s\n
+++ SYMPTOMSD MESSAGE RECEIVED +++
read_symptoms_from_q: entry
 sc_id                  %x\n
```
