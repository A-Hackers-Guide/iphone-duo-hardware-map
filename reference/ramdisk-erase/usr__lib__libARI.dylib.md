# `/usr/lib/libARI.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 6,083,184 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2704)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/usr/lib/libARI.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8, weak)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (9,468)

First 2,500 of 9,468.
```
%s: (%s:%d) Received filer initiator %s, but it is not handled
%s: (%s:%d) MemAlloc failed for TLV
%s: (%s:%d) Client(0x%04x: %s) exit-LPM
%s: (%s:%d) Unimplemented handler type %u
%s: (%s:%d) Attempt to release non-existent STREAM transaction 0x%04x
%s: (%s:%d) Trying to stop an unregistered client(0x%x). Ignored
%s: (%s:%d) Wakeable set for %s before all-ready.  IndicationReregistrationActor will request when baseband is ready.
%s: (%s:%d) Successfully registered indication %s to wake AP via ctx 0x%x
%s: (%s:%d) No blocked message for ctx 0x%x (cur %zu max %u)
%s: (%s:%d) Creating XPC client
%s: (%s:%d) Message(%s)'s mandatory TLV (%d) not packed!
%s: (%s:%d) tlv(%s) not found under msg(%s)
%s: (%s:%d) DeregIndication: gmid (%d-0x%x) is not registered with any handler (for %s cid 0x%x)
%s: (%s:%d) Request to set %s as NON-wakeable.  Ignoring...
%s: (%s:%d) Trapping: %s @ %s:%d
%s: (%s:%d) Recording indicationRegId as 0x%x
%s: (%s:%d) Received filer initiator %s, but it indicates a failure.  Skipping.
%s: (%s:%d) Tlv with g(%d) m(0x%03x) tid(%d) has len(%d) beyond end of msgBuf, message dropped
%s: (%s:%d) Exhausted lenth %d bytes but failed to find header magic word.
%s: (%s:%d) Failed to lock on AriHost instance. Shutting down?
%s: (%s:%d) Attempt to release non-existent transaction 0x%04x
%s: (%s:%d) client cid 0x%x attempting to set wakeable flag but is not registered
%s: (%s:%d) %d is out of bound for the manager [%d %d]
%s: (%s:%d) hdr->groupId = 0X%04X
%s: (%s:%d) client(0x%x): Transactions exhausted
%s: (%s:%d) Reregistering indication %s using cid 0x%x
%s: (%s:%d) Timeout waiting for registration response
%s: (%s:%d) freed as (%p)
%s: (%s:%d) Mandatory tlv with tid(%d) v(%d) is missing
%s: (%s:%d) Corrupt or invalid message - cannot extract context id
%s: (%s:%d) Attempt to release transaction for unregistered client, ctx 0x%04x.  Ignoring...
%s: (%s:%d) Reassigning ClientData from cid 0x%x to cid 0x%x
%s: (%s:%d) Extracted tlv %s(%d) len(%d) v(%d)
%s: (%s:%d) Pack tlv(%s) with tid(%d) size (%zu) raw(%p) for (%s)
%s: (%s:%d) %s: ARI_RT_ENTER_LPM: canceling low-priority flush timer and flushing requests
%s: (%s:%d) filer transfer complete: %s
%s: (%s:%d) Successfully set wakeable attribute(s) with status %d via request GMID 0x%x
%s: (%s:%d) tid (%d) is not found under gid(%d) mid (0x%03x) with defined sz(%zu)
%s: (%s:%d) cancelling blocked requests for cid 0x%x
%s: (%s:%d) BUG: Clearing %zu cancelled-but-not-released requests for cid %u
%s: Bin=[%{sensitive,libTelephonyDecoder:ARI}.*P]
%s: (%s:%d) Client (0x%x) cancelTrx(0x%x) done (took too long)
%s: (%s:%d) Ari server initialized; reconnect...
%s: (%s:%d) %s: flushing requests
%s: (%s:%d) Invoked with illegal buffer(%p) or size(%u)
%s: (%s:%d) REQ(%s) added in [%s]
%s: (%s:%d) dequeue blocked msg %s
%s: (%s:%d) %s delay(%d) exceeds warning level(%d) 
%s: (%s:%d) first sysctl() failed with err = %d
%{public}s: %{public}s
%s: (%s:%d) Already tracking 0x%x.  Likely due to reuse of transaction ID.
%s: (%s:%d) id(%08d-0x%08x) ts:%d
%s: (%s:%d) aborted %zu items [%s]
%s: (%s:%d) %d is already freed
%s: (%s:%d) Merge with upper[%d %d]
%s: (%s:%d) malloc failed for proc list
%s: (%s:%d) allocated %p for owner %s
%s: (%s:%d) Invalid msg or input value v(%p)!
%s: (%s:%d) Failed to deregister actor %s with CID 0x%x
%s: (%s:%d) No deferred indication registrations
%s: (%s:%d) Filer transaction [cid=0x%x, trx=0x%x] appears to have exited too early!  Check if it was cancelled
%s: (%s:%d) INVALID msgBuf (%p) or validSz(%d) is smaller than header
%s: (%s:%d) Failed requested len (%zu)
%s: (%s:%d) Unrecognized Filer transaction [cid=0x%x, trx=0x%x] in flight.  Likely due to unknown filer message. ari_sdk_prop may need to be updated\n
%s: (%s:%d) ctx 0x%x expected to be Filer transfer %s, but is a non-Filer response message [%s].  Discarding transfer...
%s: (%s:%d) Transferring stored ClientData from cid 0x%x to cid 0x%x
%s: (%s:%d) flushing %zu items [%s]
%s: (%s:%d) Range assignment too large(%p), got(%ld) max(%ld)
%s: (%s:%d) Pack tlv(%s) with tid(%d) len(%zu) with offset(%d) within param(%p)
%s: (%s:%d) Transaction no longer exist for ctx 0x%04x; ignoring cancel for %s
%s: (%s:%d) Dropping optional TLV(%s) for MSG(%s) with packed sz(%zu) not multiple of element encoded size(%zu)
%s: (%s:%d) Found tid(%d) under gid(%d) mid(0x%03x) wrong sz(%zu) exp (%zu)
%s: (%s:%d) tid(%d) not found under gid(%d) mid(0x%03x)
%s: (%s:%d) GetBufCtx Invalid CTX(0x%08x)
%s: (%s:%d) Trying to exit LPM for an unregistered client(0x%04x). Ignored
%s: (%s:%d) unknown notification %u
%s: (%s:%d) queue blocked msg %s
%s: (%s:%d) tid (%d) is not found under gid(%d) mid(0x%x)
%s: (%s:%d) AriMsg::unpack invalid Msg or input buff (%p)!
%s: (%s:%d) Actor %s failed to register events and/or indications
%s: (%s:%d) Failed to register client %s
%s: (%s:%d) stalling clients
%s: (%s:%d) Marking indication cid 0x%x as 0x%x
%s: (%s:%d) Destroy transaction manager for cid 0x%x
%s: (%s:%d) Unblocking for ctx 0x%x (cur %zu max %u) %s
%s: (%s:%d) XPC connection interrupted
%s: (%s:%d) Mandatory TLV id(%d) not present for msg (%s). Mark this msg invalid
%s: (%s:%d) %s: ARI_RT_CONNECTION_ERROR: canceling low-priority flush timer
%s: (%s:%d) Found %zu deferred indication registrations.  Updating RT now.
%s: (%s:%d) Multicast[%u] indication %s to cid(%d) q(%s)
%s: (%s:%d) Updating max outstanding for cid 0x%x from %u to %u
%s: (%s:%d) cancelling %zu items [%s]
%s: (%s:%d) Found magic word @index %d but usefulSz (%zu) is too small for a header.
%s: Bin=[%{libTelephonyDecoder:ARI}.*P]
%s: (%s:%d) %s: ARI_RT_EXIT_LPM
%s: (%s:%d) failed to abort blocked requests for cid 0x%x
%s: (%s:%d) %lu client reconnections are not complete at All-Ready event
%s: (%s:%d) Updating handler CID (0x%x -> 0x%x) for %s
%s: (%s:%d) Invalid response size %lu\n
%s: (%s:%d) Client registration no longer exists for cid 0x%x.  Failed re-registration
%s: (%s:%d) Transferring indication cid marked as 0x%x back to cid 0x%x
%s: (%s:%d) Skipping re-registration of indication %s as no client is registered for it
%s: (%s:%d) Reporting error for cid 0x%x: %s
%s: (%s:%d) Attempt to release a STREAM transaction associated with an automatic transaction (%s cid 0x%x ctx 0x%x)
%s: (%s:%d) Client %s (0x%x) de-registering %s (%d-0x%x)
%s: (%s:%d) No wakeable attributes to register
%s: (%s:%d) %s(%d-%x) already in %s
%s: (%s:%d) Start over @index %d to scan header magic byte0 0X%02X.
%s: (%s:%d) tid (%d) is not found under gid(%d) mid(0x%03x)
%s: (%s:%d) Aborting transactions for cid 0x%x
%s: (%s:%d) No handling block for trx 0x%04x from ctx 0x%08x
%s: (%s:%d) canceling ctx 0x%x gmid 0x%x %s
%s: (%s:%d) deregister cid 0x%x
%s: (%s:%d) Client (0x%x) cancelTrx(0x%x) done
%s: (%s:%d) No indications to push for %s using cid 0x%x
%s: (%s:%d) setting indication %s as wakeable
%s: (%s:%d) ResMgr(%p) dump total entries: %zu
%s: (%s:%d) Invalid msg or input value v(%p) s(%zu)!
%s: (%s:%d) msg(%p) with g(%d) m(0x%03x) msg-size def(%d) actual(%d)
%s: (%s:%d) Max outstanding for cid 0x%x already at %u
%s: (%s:%d) waiting for registration reply to come back: %s
%s: (%s:%d) hdr->length  = 0X%03d
%s: (%s:%d) cid (0x%x) is not registered
%s: (%s:%d) Sending for cid 0x%x (cur %zu max %u) %s
%s: (%s:%d) parkedRangeSet is used for allocation.
%s: (%s:%d) New upper free range %d
%s: (%s:%d) Setting indication %s to wake AP failed via ctx 0x%x. Unexpected message id in response (%d-0x%x)
%s: (%s:%d) error while stopping cid 0x%x
%s: (%s:%d) %s
%s: (%s:%d) hdr->ctx     = 0X%04X
%s: (%s:%d) Client(0x%04x) ignoring exit-LPM done: client has deregistered, or not yet reregistered
%s: (%s:%d) Registering %u wakeable attributes
%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
%s: (%s:%d) Client(0x%04x: %s) exit-LPM done
%s: (%s:%d) First free after a full allocation %d
%s: (%s:%d) Received client id 0x%x for %s
%s: (%s:%d) Cancelling transaction for context id 0x%04x for %s
%s: (%s:%d) Invalid msg ID definitions!
%s: (%s:%d) Attempt to release transaction on STREAM for unregistered client, ctx 0x%04x
%s: (%s:%d) Received indication %s gmid (%u) has not registered with any handler
%s: (%s:%d) Baseband is ready by the time we pushed indications; register them right away
%s: (%s:%d) Merg middle lower[%d %d] upper[%d %d]
%s: (%s:%d) Found ARI_IPC_HEADER @index %d but usefulSz (%zu) is too small for a msg->len(%zu).
%s: (%s:%d) hdr->magic   = 0X%08X
%s: (%s:%d) client 0x%x did not start in %dms.  Likely client queue is stuck or stalled!
%s: (%s:%d) Blocking for cid 0x%x (cur %zu max %u blocked %zu) %s
%s: (%s:%d) Found received trx 0x%x on cancelled list
%s: (%s:%d) Invalid tlv value found for msg(%s)!
%s: (%s:%d) Grp(%d) m(0x%03x) pos(%d) tid(%d) with offset(%d) + len(%zu)*dim(%d), but param sz is only (%zu)
%s: (%s:%d) Failed to register %s
%s: (%s:%d) Filer initiator response detected but filer ctx 0x%x is already in flight!
%s: (%s:%d) Client no longer exist for ctx 0x%04x; ignoring cancel for %s
%s: (%s:%d) Client(0x%04x) registering %s (%d-0x%x)
%s: (%s:%d) FilerTransfer %s has been abandoned with %lld bytes remaining of %lld total bytes
%s: (%s:%d) Tlv(%s) Grp(%d) m(0x%03x) pos(%d) tid(%d) w/ offset(%d) rawlen(%zu) into max origLen(%zu) param sz(%zu)
%s: (%s:%d) %s: ARI_RT_STOP: canceling low-priority flush timer
%s: (%s:%d) Client 0x%x did not stop in %dms.  Likely client queue is stuck or stalled!
%s: (%s:%d) id(%08d-0x%08x) ts:%u
%s: (%s:%d) Lower free range merged %d
%s: (%s:%d) Sending reply for cid 0x%x event %s
%s: (%s:%d) Aborting new request from cid 0x%x: %s
%s: (%s:%d) Found max outstanding count after releaseTrx ctx 0x%x (cur %zu max %u) for CID 0x%x
%s: (%s:%d) Upper free range merged %d
%s: (%s:%d) New lower free range %d 
%s: (%s:%d) Trying to start an unregistered client(0x%x). Ignored
%s: (%s:%d) Pushing all indications for %s using cid 0x%x [%lu]
%s: (%s:%d) Received NACK for setting wakeable attribute
%s: (%s:%d) Client(0x%04x) stop done
%s: (%s:%d) Reassigning indications using cid 0x%x to use 0x%x
%s: (%s:%d) failed to cancel blocked requests for cid 0x%x
%s: (%s:%d) Host Success!
%s: (%s:%d) Dropping ind(%d-0x%x): Client(0x%04x) is no longer registered
%s: (%s:%d) error cancelling ctx 0x%x gmid 0x%x %s
%s: (%s:%d) Unexpected response message 0x%x
%s: (%s:%d) Registering AriHost actors
%s: (%s:%d) clientCtxId(0x%08x) or cid(0x%08x) has not registered with AriHost
%s: (%s:%d) No dispatch queue for cid 0x%04x from ctx 0x%08x
%s: (%s:%d) Timeout waiting on dispatch group!
%s: (%s:%d) Trying to enter LPM for an unregistered client(0x%x). Ignored
%s: (%s:%d) no blocked requests to cancel for cid 0x%x
%s: (%s:%d) trying to unpack mandatory TLV(%s) for MSG(%s) with packed sz(%zu) not multiple of element encoded size(%zu)
%s: (%s:%d) %s: waited %u seconds and did not reach idle, flushing low-priority queue anyway
%s: (%s:%d) Deallocated cid(0x%x) based on ARICtxId(0x%08x)
%s: (%s:%d) Flushing %s
%s: (%s:%d) Client(0x%04x) start done (took too long)
%s: (%s:%d) Client(0x%04x) stop
%s: (%s:%d) name(%p) or cid(%p) is NULL
%s: (%s:%d) Extract msg from (msgBuf=%p) on obj(%p)
%s: (%s:%d) Attempt to de-register non-existant client ID 0x%x
%s: (%s:%d) cancelling host stalled requests and stalling client work queue
%s: (%s:%d) Client(0x%04x: %s) enter-LPM done
%s: (%s:%d) Invalid cid received: 0x%x
%s: (%s:%d) File write stream completed, but no active transfer found! ctx 0x%x
%s: (%s:%d) Actor %s with CID 0x%x failed to deregister
%s: (%s:%d) New registered client ID is identical to the previous one (0x%x). No update needed.
%s: (%s:%d) Received identical cid 0x%x.  Transferring stored ClientData
%s: (%s:%d) cid 0x%x not registered
%s: (%s:%d) failed to abort [low-prio] stalled requests for cid 0x%x
%s: (%s:%d) AriMsg(id) INVALID input gid(%d) mid((%03x)
%s: (%s:%d) MemAlloc failed for TLV buffer
%s: (%s:%d) trying to unpack mandatory TLV(%s) for MSG(%s) with packed sz(%zu) > defined max encoded size(%zu)
%s: (%s:%d) Unpack tlv(%s) with tid(%d) raw(%p) len(%zu) into origLen(%zu) for g(%d) m(0x%03x)
%s: (%s:%d) Received mismatched GMID for setting wakeable attribute
%s: (%s:%d) Client %s (0x%x) registered %s (0x%x)
%s: (%s:%d) Client is setting indication %s explicitly as NON-wakeable.  This should be avoided.
%s: (%s:%d) Destroying non-empty AriHost [%s] (%s)! %u items remain
%s: (%s:%d) REQ(%s) not allowed during stall [%s]
%s: (%s:%d) Dropping optional TLV(%s) for MSG(%s) with packed sz(%zu) > defined max encoded size(%zu)
%s: (%s:%d) %s: ARI_RT_START
%s: (%s:%d) %s: detected relatively idle ARI traffic in iteration %u; flushing low-priority queue
%s: (%s:%d) Failed to de-register client 0x%x
%s: (%s:%d) Cid (0x%08x) allocate trx 0x%08x ctx = 0x%08x blk 0x%08lx
%s: (%s:%d) RegIndication: Client(0x%04x) has not been registered
%s: (%s:%d) Setting indication %s to wake AP failed via ctx 0x%x (Received NACK with reason %s)
%s: (%s:%d) Received tlv with g(%d) m(0x%03x) tid(%d) len(%d) > exp(%zu), ignored
%s: (%s:%d) trying to pack gid(%d) mid(0x%03x) tid(%d) with sz(%zu) > max size(%zu)
%s: (%s:%d) hdr->msgId   = 0X%04X (%s)
%s: (%s:%d) Client(0x%04x) stop done (took too long)
%s: (%s:%d) Failed to lock on AriHost instance
%s: (%s:%d) Checking for item 0x%x in queue when not stalled! [%s]
%s: (%s:%d) %s: Can not find gmid(%d-%x) in SDK
%s: (%s:%d) second sysctl() failed with err = %d
%s: (%s:%d) client 0x%x did not cancelTrx(0x%x) in %dms.  Likely client queue is stuck or stalled!
%s: (%s:%d) Setting indication %s to wake AP failed via ctx 0x%x (Received NACK, reason unknown due to malformed NACK)
%s: (%s:%d) New independent middle range %d
%s: (%s:%d) Scanned total %d bytes and found header magic word.
%s: (%s:%d) Data with valid magic but illegal size (%d). Ignoring...
%s: (%s:%d) %s: too busy to flush low-priority queue: iteration %u Msg/second=%llu
%s: (%s:%d) Skipping additional %d bytes and found header magic byte0 0X%02X.
%s: (%s:%d) Version mistmach for tlv with g(%d) m(0x%03x) tid(%d), got(%d) expecting(%d), ignored
%s: (%s:%d) ExitTrx() is deprecated.  Attempt to exit transaction ID 0x%04x.  Ignoring...
%s: (%s:%d) Setting %s as wakeable using cid 0x%x
%s: (%s:%d) MemAlloc failed for buffer sz (%zu)
%s: (%s:%d) Invalid context id 0x%x
%s: (%s:%d) new filer transfer: %s
%s: (%s:%d) indicationRegId not set.  Deferring RT registration of %s (%d-0x%x).  Total deferred: %zu
%s: (%s:%d) Client(0x%04x) start
%s: (%s:%d) Couldn't unpack response for setting wakeable attribute
%s: (%s:%d) failed to flush stalled requests for cid 0x%x
%s: (%s:%d) Create transaction manager for cid 0x%x
%s: (%s:%d) Received filer initiator %s, but corresponding size info is not found.  Skipping.
%s: (%s:%d) INVALID msgbuf (%p) len(%zu)
%s: (%s:%d) Actor '%s' received RT re-init event
%s: (%s:%d) Client(0x%04x: %s) enter-LPM
%s: (%s:%d) no client handlers are registered for this indication, %s.  setting wakeable metadata only
%s: (%s:%d) Putting aside ClientData for %s cid 0x%x.
%s: (%s:%d) failed to cancel stalled requests for cid 0x%x
%s: (%s:%d) releasing %p for owner %s
%s: (%s:%d) Message(%s) size (%d) is larger than max (%d)
%s: (%s:%d) Failed to send AriGrpMsgsAttribReq
%s: (%s:%d) %s: received %lld bytes more than expected in filer transfer (total size %lld)\n
%s: (%s:%d) Duplicated TLV id %d
%s: (%s:%d) Clearing transaction manager for cid 0x%x
%{public}s: Bin=[%{public,libTelephonyDecoder:ARI}.*P]
%s: (%s:%d) msgBuf (%p) with invalid magic (0X%X) or an incomplete msg got(%d) exp(%zu)
%s: (%s:%d) Decode  %s(%d-0x%03x) len(%zu) buf(%p) trx(0x%08x)
%s: (%s:%d) Allocated cid(0x%02x) ARICtxId(0x%08x) client(%s) maxOutstandingReqs(%d)
%s: (%s:%d) Registration failed for client %s: %s
%s: (%s:%d) trying to pack gid(%d) mid(0x%03x) tid(%d) with sz(%zu) not multiple of element sz(%zu)
%s: (%s:%d) Failed to lock on AriHost instance!!
%s: (%s:%d) Failed client deregistration with RT for cid 0x%x
%s: (%s:%d) CopyEncodedMessage fails on msg(%p)
%s: (%s:%d) NACK received during Filer transfer %s.  Discarding transfer...
%s: (%s:%d) Client(0x%04x) ignoring enter-LPM done: client has deregistered, or not yet reregistered
%s: (%s:%d) Encode  %s(%d-0x%03x) len(%zu) buf(%p) tlv(%d) obj(%p)
%s: (%s:%d) Register called twice on %s
%s: (%s:%d) %s free ctx 0x%04x
%s: (%s:%d) flushing host
%s: (%s:%d) parkedRangeSet is checked for allocation on %d.
%s: (%s:%d) Transferring indication cid marked as 0x%x to new cid 0x%x
%s: (%s:%d) Creating GCD client
%s: (%s:%d) unknown command 0x%llx
%s: (%s:%d) UNKNOWN tlv with g(%d) m(0x%03x) tid(%d), ignored
%s: (%s:%d) failed to abort [normal] stalled requests for cid 0x%x
%s: (%s:%d) Invalid indication size %lu\n
%s: (%s:%d) targetSet is empty! This is likely not invoked atomically
%s: (%s:%d) Merge with lower[%d %d] 
%s: (%s:%d) Setting indication %s to wake AP failed via ctx 0x%x (Failed to extract)
%s: (%s:%d) Client %s (0x%x) has %lu indications registered
%s: (%s:%d) Notify event %s failed for cid %u
%s: (%s:%d) tid(%d) has offset(%d) and len(%zu) outside of param with sz(%zu)
%s: (%s:%d) Attempt to release ctx 0x%04x.  Ignoring...
%s: (%s:%d) Client(0x%04x) start done
%s: (%s:%d) Reregistering all indications for %s using cid 0x%x
%s: (%s:%d) Id from AriMsg header in buffer @(%p) not found in SDK
%s: (%s:%d) AriMsg::unparam invalid input AriMsg (%p) or  bufferr (%p)!
%s: (%s:%d) Fatal to send requests against transaction manager of cid 0x%x
%s: (%s:%d) Client %s has NO indications registered
%s: (%s:%d) aborting %s
%s: (%s:%d) Attempt to remove gmid(%d-%x) not in %s
t_s_UtaIdcRTScanFreqConfig
IBI_SMS_UNIDENTIFIED_SUBSCRIBER
(%s:%d) Creating GCD client
IBI_CDMA_SMS_ERR_CAUSE_MISSING_EXP_PARAM
IBI_SIM_MEMORY_EXCEEDED
IBI_SS_GSM_ERROR_NO_ROUTE
cdma_evdo_scell_info_t21
IBI_IMS_ME_RTCP_SDES_NAME
IBI_NET_BAND_NR_30
IBI_SIM_HW_EVENT_INOUT_DEBOUNCE_TIMEOUT
lte_scell_info_ext_t28
IBIGetSimMuxCfgReq
IBI_CALL_CS_ERROR_CAUSE_CDMA_TC_RELEASE_TIMEOUT
IBI_CALL_PS_RESULT_CODE_WIRELINE_ACCESS_AREA_NOT_ALLOWED
IBI_SIM_TK_PROACTIVE_CAUSE_SMS_RP_ERROR
is_sat_system_t37
IBI_CALL_CS_BURST_DTMF_WIDTH_350MS
VINYL_CAP_VIRTUAL_HYDRA_CAPABLE
/Library/Caches/com.apple.xbs/E497E93F-14A7-4885-82BD-D54E476F8AAB/TemporaryDirectory.ZrAZ7x/Sources/AppleRemoteInvocation/common/src/ari.cpp
IBI_IMS_ME_AUDIO_CODEC_TYPE_G711A
IBI_NET_DC_SERVICE_DOMAIN_IMS
[unregistered client]
IBI_CELL_INVALID_NETWORK
IBI_NET_EVDO_RADIO_SIGNAL_REPORT_CONFIG_PRESENT
IBI_SIM_BER_TLV_TYPE
IBI_STW_CAUSE_UNSUPPORTED_IN_CURRENT_CONNECTION_STATE
IBI_NET_BAND_LTE_85
IBI_SMS_MS_FAILURE_UNSPECIFIED
IBISimGetMsgListRspCb
CsiIceAudSetMuteStatusRespCb
enable_flag_t1
wakeup_info_t2
IBICbsGetConfigReq
IBIMapModemInstanceToSimReq
IBI_OGRS_RESULT_MAX
bIPAddrAllocNasSignaling_t92
IBIImsMERtcpSDESReportIndCb
generated_app_key_t2
IBI_CALL_CS_NO_CALL_ERROR
IBI_LP_FIX_TYPE_3D
procedure_result_t2
app_type_t6
TraceFlushReq
IBIOgrsMasterLikelihood
CsiIceSarWaitTimeRspCb
IBI_NET_EONS_SUPPORT_FALSE
IBI_SIM_CHV2_REQUIRED
CsiIdcRTSetLinkQualityReportConfigReq
config_t3
IBI_CALL_PS_DNS_PROT_TLS
IBIPeriodicFloatDoubleIndCb
IBI_SIM_PB_RESULT_ERROR_NO_CHV_INITIALIZED
IBI_SIM_TOOLKIT_BUSY
TraceGetConfigReq
intra_freq_info_t4
IBI_SS_LCS_POS_CAP_CP_LOCATION_REQUEST_SUPPORT
IBICpsSetCellularRadioStateRspCb
TRANSMIT_STATE_INFO_DISABLED
IBI_CDMA_LANGUAGE_PUNJABI
IBI_SS_GSM_ERROR_FACILITY_NOT_IMPLEMENTED
moringa_data_t20
switch_toggled_t2
state_t2
IBI_EOS_ASSERTION_NO_RESET_ACQUIRE
IBI_NET_BAND_GSM480
IBI_SMS_MN_TIMEOUT
CsiIceSecSendRFSelfTestTicketRspCb
UtaIdcSetRTFeatureSpmiTxReqV3
IBIStwDataMsgTxCancelReq
IBI_CALL_PS_DELIVERY_ORDER_SUBSCRIBED
IBI_CLS_POS_CAP_GNSS_AD_BDS
IBI_LP_GANSS_DOPPLER_UNCER_EXT_NO_INFO
IBI_SIP_EVENT_SESSION_FAILURE
IBI_SS_NET_ERROR_LONG_TERM_DENIAL
IBIOgrsDeactivationReq
IBI_CDMA_SMS_ERR_CAUSE_DELIVERY_POSTPONED
IBICallPsDataPathCleanupReq
mode_pref_t3
uicc_result_t4
IBI_NET_BAND_NR_71
31_embms
ARI_ATTR_BUFFER_LAST
IBIMsNetIceCsgAsfSearchReq
is_china_sku_t8
slot_id_t4
IBI_IMS_ME_AUDIO_CODEC_TYPE_AMRWB
IBI_STW_UX_CONGESTION_STATUS_SEVERE_CONGESTION
wlanMeasurements_t5
ims_cc_data_t3
IBIEmbmsServiceIndCb
CsiIceTemperatureRspCb
(%s:%d) releasing %p for owner %s
IBI_CALL_CS_BLACKLIST_FULL_NO_AUTO_CALL_ATTEMPTS
IBI_NET_AP_SCREEN_STATUS_OFF
IBI_NET_CELL_SIB2_BARRING_CONFIG
IBI_SMS_TP_FCS_ERROR_IN_MS
IBI_CDMA_LANGUAGE_GUJARATI
IBI_NET_FD_DISCARD_CAUSE_DETACH
lte_scell_info_len_t15
lte_scell_info_t16
IBI_NET_BAND_NR_74
IBI_SIM_TK_BC_REPEAT_INDICATOR_SCUD_IF
unpers_ftab_hash_t2
select_item_t13
interested_sai_list_t11
IBI_SIM_SEARCH_RECORD_00_PATTERN
gsm_ncell_info_valid_t20
(%s:%d) Register called twice on %s
IBICallPsNwSlicingRegStatusInfoReq
bPcscfIPv6_t10
ims_sms_t4
IBI_CALL_PS_VOIP_CALL_FINISH
IBI_SMS_TP_FCS_SC_SYSTEM_FAILURE
sw_dbug_trap
roaming_t3
IBI_SIM_TK_PROACTIVE_CAUSE_MULTIPLE_CARD_COMMANDS_ERROR_SPECIFIED_READER_NOT_VALID
IBI_CALL_CS_UNEXPECTED_MSG_TYPE
IBI_CALL_PS_SUSPEND_CAUSE_GPRS_HOLD_SMS
IBI_SIM_CMD_RECORD_NOT_FOUND
chv1_status_t18
alpha0_t2
CsiMsCpsReadMeidRspParam
lte_scell_info_r15_t52
IBICallCsVoimsSrvccHoStatusIndCb
IBIEnableVirtualSimRspCb
IBI_LP_ABORT_NETWORK
IBI_SS_LCS_GANSS_ID_MOD_GPS
eap_msg_t4
IBI_SIM_TK_PROACTIVE_CAUSE_COMMAND_DATA_NOT_UNDERSTOOD_BY_ME
IBIPsFilterRespCodeType
CsiBspNvmReadGroupRespCb
IBINetPlmnId
proximity_indicator_t3
IBIStwMmcDumpConfigRspCb
IBI_NET_PLMN_PRIORITY_INFO_TYPE_IPLMN
ant_tuner_state_t2
IBINetIceCellularSwitchStatusReq
refresh_performed_t3
IBI_SMS_UNSENT
IBI_NET_BAND_CDMA_5
CsiIceSarWaitTimeReq
IBI_SIM_PB_LINK_TYPE_TYPE_1_LINK
IBI_SMS_MS_CONN_REL_LOWER_LAYER_FAILURE_DL
IBI_CALL_CS_SIMTK_SETUP_REJ_PENDING_SIMTK_SETUP
IBI_CALL_CS_TEMP_FORBIDDEN_CALL_ATTEMPT_NO_SERVICE
IBI_CALL_PS_RESULT_CODE_DUAL_SIM_CONFLICT
IBI_NET_PLMN_NAME_INFO_RESULT_SUCCESS
max_packetization_interval_t10
IBICallCsExtEccListParam
IBIVinylLPASigningRspCb
IBI_CALL_PS_PEAK_THROUGHPUT_16K
IBI_SIM_HW_EVENT_INOUT_INSERTED
IBISimAccessApduCmdRspData
IBICallPsLoopbackResult
CsiIceSpeakerStateRspCb
InterfaceID_t3
CsiXsioGetRspCb
containsCtx
IBI_CALL_PS_RESULT_CODE_INSUFFICIENT_RESOURCES
IBI_NET_BAND_LTE_67
IBI_NET_BAND_LTE_9
(%s:%d) clientCtxId(0x%08x) or cid(0x%08x) has not registered with AriHost
IBINetRatUnavailableRanDatabaseRsp
IBI_CALL_PS_RESULT_CODE_ERR_INVALID_CID
IBI_NET_ERROR_MS_IDENTITY_CANNOT_BE_DERIVED_BY_THE_NETWORK
IBI_SMS_ABNORMAL_RELEASE_NO_ACT_ON_RADIO_PATH
app_id_t5
IBI_SIM_TK_PROACTIVE_CAUSE_COMMAND_PERFORMED_WITH_MISSING_INFORMATION
velocityTypes_t21
IBICallCsCmd
tx_ant_location_t1
is_cs_rej_internal_t25
local_phone_book_t5
IBIStwServicePriorityUpdateRspCb
IBI_CALL_PS_RESULT_CODE_CANNOT_DEACTIVATE_ATTACH_APN
IBI_CALL_CS_UNRECOGNIZED_LINKED_ID
CsiDelayedOutstandingResp
IBICallPsGetDataBearerInfoReq
bDSMIPv6_haar_t64
IBIPsProtoType
IBISimTkAlphaIdentifier
IBINetNssaiInfoIndCb
IBI_CALL_PS_MEAN_THROUGHPUT_500
IBI_CALL_PS_UL_SDU_NO_SCALING_SET
IBI_CALL_PS_VOIP_APP_3RD_PARTY
IBI_SIM_TK_PROACTIVE_CAUSE_ACCESS_TECHNOLOGY_CANNOT_PROCESS_COMMAND
IBI_SMS_TP_INVALID_TIME_STAMP
IBI_SS_LCS_VELOCITY_TYPE_HORIZONTAL_VELOCITY
IBIPriRefreshReq
enable_data_t8
AriRuntimeNotifyAck
Latency_Value_t4
(%s:%d) Pushing all indications for %s using cid 0x%x [%lu]
CsiBspShutdownRspCb
IBIMsLpPosLocationRequestStatusIndCb
report_nr_serv_cell_type_t10
ul_freq_info_ext_t12
host.hostQueue == nullptr
nr_band_status_t11
user_reboot_t3
IBIAccHoppingFreqBandwidthInfo
(%s:%d) queue blocked msg %s
IBINetDcImsRegistrationStatusInfoReq
pin_required_for_update_t7
em_param_t5
IBI_STW_V2_CAUSE_OPRT_MODE_NOT_READY
acquisition_t5
media_type_t3
call_control_result_t3
IBISimSecAuthKc
IBINetRatModeStatusIndCb
IBI_CALL_PS_NOTIFICATION_INDICATOR_SRVCC_HANDOVER_CANCELLED
ICE_SIM_TEST_CMD_NULL
IBIPeriodicCounterBufferLastIndCb_v3
IBISsIdentificationReq
cbs_service_ready_t2
IBI_CALL_PS_STOP_DATA_CALL_REASON_INVALID
IBI_NVM_DYNAMIC
radioSignalReportingConfigPresenceBitmask_t2
IBI_NET_AP_STATUS_INVALID
IBI_NET_BAND_NR_6
IBI_NET_ERROR_NON_3GPP_ACCESS_TO_5GCN_NOT_ALLOWED
IBIStwS4ConfigData
IBI_NET_REGISTRATION_REJECT_CAUSE_NO_CARRIER
IBI_NET_USE_OF_DC_WITH_NR_IS_RESTRICTED
(%s:%d) %d is already freed
(%s:%d) Found ARI_IPC_HEADER @index %d but usefulSz (%zu) is too small for a msg->len(%zu).
IBI_CALL_CS_MS_REEST_FAILURE
IBI_CLS_POS_CAP_LTE_SON_LOCATION_AGE_LIMIT
IBISimTkGetInputRspParam
IBICallCsVoimsANBRProhibitTimerReq
IBI_CALL_PS_DATA_BEARER_INFO_5G_SUB6
IBI_CLS_OPERATION_TYPE_GET
CsiAwdsMetricSubSwitchReq
bad_num_frames_t9
AriGrpMsgsAttribResp
IBI_SMS_MSG_WAIT_SET_INACTIVE
IBISimPbResult
is_always_on_t42
skip_fdn_check_t16
CsiIceAntennaPrefReq
IBICallPsPdpContextId
filter_cmd_t4
cb_list_length_t6
t_s_UtaIdcCellConfigV2
IBI_LP_GNSS_TO_ID_QZSS
IBI_OGRS_FAILURE_CAUSE_NotEnabled
IBI_SIM_PIN2_APP6_KEY
IBI_NET_BAND_NR_28
gsm_ncell_info_t15
updateBytesReceived
IBI_CALL_CS_MS_TIMEOUT
gid1_slot2_t16
IBI_NET_BAND_UMTS_XXII
IBI_NET_CELL_LTE_BARRING_STATUS_TYPE_EMERGENCY
IBI_NET_ERROR_MESSAGE_NOT_COMPATIBLE_WITH_PROTOCOL_STATE
IBI_SS_NET_REJECT_UNEXPECTED_ERROR
min_rec_count_for_search_t7
(%s:%d) Attempt to de-register non-existant client ID 0x%x
CsiSecGetRFSelfTestNonceReq
 expected 
IBI_CALL_CS_CLI_NOT_AVAILABLE
IBI_CALL_CS_SIMTK_SETUP_REJ_TIME_OUT
IBI_SIM_FCP_FILE_STATUS_ACTIVATED
rtlibHandle == NULL
cell_id_t3
simtk_transaction_id_t3
IBI_CLS_POS_CAP_NR_ECID_SUPPORT
p_header_array_t2
IBIStwActivateRspCb
IBI_ERROR_INVALID_PARAM
IBI_NET_BAND_LTE_103
IBI_SIM_TK_PROACTIVE_CAUSE_BEARER_INDEPENDENT_PROTOCOL_ERROR_SERVICE_IDENTIFIER_UNKNOWN
VINYL_CAP_TAPE_CAPABLE
search_rec_info_t10
bDnsIPv4_t95
IBICallPsQfi
IBIAccSearchFreqBandwidthInfo
IBI_LP_MEASRSP_INVALID
(%s:%d) client cid 0x%x attempting to set wakeable flag but is not registered
(%s:%d) Wakeable set for %s before all-ready.  IndicationReregistrationActor will request when baseband is ready.
event_t3
ignore_duplicates_t5
IBI_NET_BAND_GSM900_E
IBI_NET_BAND_LTE_13
IBI_NET_PWR_CLASS_DEFAULT
IBI_SIM_PB_RESULT_ERROR_NO_EF_CHOOSEN
VINYL_CAP_INVALID
alpha3_t5
activation_pubkey_hash_t2
lo_ntp_t6
IBI_NET_ERROR_PROTOCOL_ERROR_UNSPECIFIED
IBI_OGRS_DISCOVERY_STATUS_SyncMasterChange
IBI_SIM_TK_PROACTIVE_CAUSE_BEARER_INDEPENDENT_PROTOCOL_ERROR_CHANNEL_IDENTIFIER_NOT_VALID
IBI_SS_LCS_POS_CAP_MDT_SON_LOCATION_SUPPORT
IBI_SS_LCS_VELOCITY_TYPE_HORIZONTAL_WITH_VERTICAL_VELOCITY
t_s_UtaIdcLaaMeasInfo
mcc_list_t3
IBIStwServiceType
IBI_CALL_CS_LINE_1
IBI_CALL_PS_RESULT_CODE_CALL_THROTTLED
IBI_CDMA_SMS_ERR_CAUSE_SS_NOT_SUPPORTED
IBINetNetworkOpMode
lte_band_status_ext_t9
IBI_NET_BAND_LTE_26
IBI_NET_BAND_NR_10
IBI_NET_SERVING_CELL
IBI_SIM_APPLICATION_DEACTIVATE_CLOSE_CHANNEL
IBI_STW_DEACTIVATION_REASON_AIRPLANE_MODE
posProtocol_t11
CsiIceSecSendRFSelfTestTicketV2RspCb
UtaIdcSetLaaConfigReq
IBI_NET_BAND_UMTS_XIX
IBISimSecRand
IBI_CALL_CS_VOIMS_MMTEL_SESSION_STARTED
IBIDeprecatedInheritedReq1
IBIQoELatencyReportReq
AbortTransactions_block_invoke
mbsfn_area_id_list_t4
iccid_t1
IBI_OGRS_EMERGENCY_TRANSMISSION_RESULT_Failure
read_card_param_t6
evs_ul_cmr_t26
(%s:%d) Failed to send AriGrpMsgsAttribReq
CsiIceAudLoopbackRespCb
no_of_plmns_t7
IBI_SS_LCS_VELOCITY_TYPE_INVALID
IBI_STW_PROTOCOL_MODE_TEST
domain_t18
IBI_CBS_CAUSE_CONFIG_PRIM_SUCCESS_SEC_FAIL
IBIFilerHSReadBBGetSizeReq
IBICallCsEmergencyNumberListIndCb
IBINetGeoMCCRspCb
bDnsIPv6_t62
event_bitmap_t2
IBI_CALL_PS_ATTACH_APN_SETTING_ROAM_1
IBI_HEALTH_ACTIVITY_SWIM_LOCATION_TYPE_MAX
IBI_OTASP_STATUS_COMMITTED
(%s:%d) %s: too busy to flush low-priority queue: iteration %u Msg/second=%llu
IBIStwOverrideConcurTmrReq
IBI_CALL_CS_PROACTIVE_SIM_APPL_TERMINATED_BY_USER
IBI_SS_NET_REJECT_RETURN_RESULT_UNEXPECTED
CsiIpcCtrlPathTestSrcCfgRspCbParam
IBIMsSsLcsPositioningCapabilityRspParam
IBI_ERROR_BAD_FORMAT
IBIPlmn
(%s:%d) ResMgr(%p) dump total entries: %zu
num_digits_t4
IBISimPbWriteRecReq
IBI_NET_DUPLEX_MODE_TDD
IBI_SMS_TP_MISSING_SC_ADDRESS
IBI_SS_GSM_ERROR_RECOVERY_ON_TIMER_EXPIRY
IBICallCsStopDtmfReq
IBI_LP_DISCARDED_POS_MSG_TYPE_ERROR
IBIFilerHSStartWriteBBSessionRspCb
IBIStwOverrideConcurTmrRspCb
IBI_CALL_PS_NR5G_NEIGHBOR_CELL_LTE
IBI_SIM_NOT_AVAILABLE
IBISimTkProactiveCmdSetupMenu_V1
IBIOgrsDeactivationRspCb
UtaChar
IBI_CALL_PS_BUTTER_MODE_DISABLED
IBI_SMS_TP_FCS_SM_TYPE_0_NOT_SUPPORTED
remote_ip_length_t8
IBINetIceFdReportIndCb
IBI_STW_V2_CAUSE_INTERNAL
(%s:%d) Found tid(%d) under gid(%d) mid(0x%03x) wrong sz(%zu) exp (%zu)
IBINetCdmaEvdoRadioSignalReportingConfiguration
support_t2
IBI_SIM_PB_LINK_TYPE_NO_LINK
wci2_power_limiting_timer_ms_t6
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
qos_rule_t4
CsiIceIpcLogBufferList
IBIFilerHSWriteBBRspCb
IBI_CALL_CS_MS_L2_CAUSE_UNSOLICITED_DM_RESP_MFES
params_t2
(%s:%d) Marking indication cid 0x%x as 0x%x
close_channel_t21
csi_bmm_bti_report_t1
IBI_CALL_CS_CALL_REJECTED
IBI_CALL_PS_RESULT_CODE_CS_DOMAIN_NOT_AVAILABLE
IBINetRatModeSetting_V1
IBINetConfigureNetworkModeError
IBI_CALL_PS_VOIP_CALL_LIVE_VOICEMAIL_FINISHED
(%s:%d) %s
IBILpLocationServerErrorCause
locationStatus_t3
IBICallPsNotificationIndCb
(%s:%d) trying to pack gid(%d) mid(0x%03x) tid(%d) with sz(%zu) not multiple of element sz(%zu)
sleep_indication_t5
IBI_CALL_CS_ERROR_CAUSE_CDMA_ORIG_NO_SERVICE_FAIL
IBI_CALL_CS_TELESERVICE_NOT_PROVISIONED
IBINetManageUePolicyCommandReject
IBI_SIM_TK_PROACTIVE_CAUSE_LAUNCH_BROWSER_ERROR
IBI_LTL_XCC_IND_TYPE_INVALID
(%s:%d) Client(0x%04x) stop done
IBIVinylFinalizePsoReq
IBI_CALL_PS_RESULT_CODE_MAC_FAILURE
IBI_SIM_TK_PROACTIVE_CAUSE_MULTIPLE_CARD_COMMANDS_ERROR_MUTE_CARD
nr_list_t9
IBISmsTpFcs
IBI_CALL_PS_VOIP_CALL_ATTEMPTED
IBI_NET_BAND_NR_15
message_id_t18
UtaIdcSetTimeSharingConfigReq
screen_status_t2
IBI_NET_BAND_LTE_72
(%s:%d) Cancelling transaction for context id 0x%04x for %s
(%s:%d) aborting %s
eutran_rel_t9
IBI_CALL_CS_SIGNAL_PITCH_RESERVED
IBI_VINYL_PRLACT_SIM_FILE_SUCI_CALC_INFO
configured_max_bw_t4
remote_ip_length_t14
rat_t3
ssac_barring_info_for_video_t5
IBI_IMS_ME_RTCP_SDES_CNAME
IBI_NET_BAND_NR_38
tty_mode_t12
CSI_ICE_MON_MEMORY_INFO_T
pssi_table_t3
cb_data_t7
IBI_CALL_CS_MTC_AS_CALL_SETUP
IBI_IMS_ME_DTMF_DIGIT_CODE_ASTERIX
session_id_t17
CsiIceSarEnableRspCb
CsiIdcTestModeParam
IBI_ERROR_INSUFFICIENT_PERMISSIONS
IBI_OGRS_FAILURE_CAUSE_NotDiscovered
IBI_SS_GSM_ERROR_SEMANTICS_INCORRECT
IBISimFileReadBinaryRspCb
IBI_NET_BAND_NR_81
IBI_NET_ERROR_PAYLOAD_NOT_FORWARDED
hysteresis_state_t3
audio_control_t21
UtaIdcSetTunerArbitrationConfigReqV3
IBINetBandSettings3gppExt
hwid_t10
IBI_CALL_CS_CALL_CHANGED_TO_SS
IBI_NET_REGISTRATION_STATUS_SERVICE_DISABLED
IBI_SS_OC_UNKNOWN
IBI_STW_CAUSE_UE_CONFIG_FILE_DECODE_FAILURE
IBIMsClsPositioningCapabilityReq
IBI_NET_DC_BARRING_FACTOR_P10
IBI_STW_V2_CAUSE_NO_MEMORY
search_opt_t7
velocityRequested_t7
CsiSecNonce
IBI_CDMA_SMS_ERR_CAUSE_NO_ACK
IBI_SIM_TK_PROACTIVE_CAUSE_BEARER_INDEPENDENT_PROTOCOL_ERROR_TRANSPORT_LEVEL_NOT_AVAILABLE
IBILpGanssNavDataGlonass
pack
send_ussd_t5
t_s_UtaIdcTxActConfig
IBINetDuplexMode
IBI_SIM_TK_COMMAND_TYPE_SEND_DTMF
IBI_SS_GSM_ERROR_MS_NO_SERVICE
ganssTodUncertainty_t5
breadModeState_t3
%11s%s%s
shutdown_type_t1
is_gprs_available_t5
forward_to_address_t8
IBIStwSetBroadcastInfoBlobRspCb
UNKNOWN
IBIVinylInitPsoRspCb
IBI_CALL_PS_ACTIVATION_STATUS_5_TIME_T3380_EXPIRY
type_t118
50_ibi_vinyl
t_s_UtaIdcTunerArbitrationConfig
IBICallCsExtEmergencyListValidity
call_pref_t3
override_data_inactivity_short_window_value_in_s_t2
IBIStwFringeCellStatus
IBIVinylPrlActRawData
IBI_CALL_CS_RETRY_CAUSE_EMERGENCY_CALL_SETUP
Quality_index_t4
CsiFlashPluginHeader
IBICallCsCdmaVerifySpcCodeReq
IBIStwGnssHeatMapParam
IBI_CALL_CS_MS_RRC_CONN_ESTABLISHMENT_FAILURE
IQCAP_ACTIVITY_STATUS_FAILED
IBI_SMS_TEMPORARY_FAILURE
com.apple.telephony.bb
IBISimSetSmsTagRspCb
IBI_SIM_TK_ENVELOPE_TYPE_EVENT_DOWNLOAD_CALL_CONNECTED
IBI_HEALTH_ACTIVITY_TYPE_CYCLE
IBI_FILER_HS_CLIENT_PRI
CsiIcePowerSourceStateRspCb
Ari::RT_STOPPED
IBI_CALL_CS_MS_INVALID_MANDATORY_INFO
IBI_SMS_TP_FCS_TOOLKIT_BUSY
IBI_LTL_XCC_IND_TYPE_SUCCESS
(%s:%d) Cid (0x%08x) allocate trx 0x%08x ctx = 0x%08x blk 0x%08lx
arfcn_t3
t_s_UtaIdcLaaConfig
is_dst_available_t6
sessionId_t9
IBISipMsgInjectToCpIMSTraceReq
IBI_SS_STATUS_CODE_QUIESCENT
ssrc_t5
CsiIceWakeupReasonReq
IBINetIqCapConfigParam
location_request_t3
IBIXccLtlReq
frac_lost_t6
IBICdma1xNeighborCellInfo
IBICbsConfigRspCb
IBI_CALL_PS_ERRONEOUS_SDU_DELIVERY_RESERVED
IBI_NET_DC_IMS_REGISTRATION_STATE_STARTED
IBI_SMS_NORMAL_CALL_CLEARING
cdma1x_ncell_info_t23
IBINetNssaiInfoReq_V2
IBIStwDeActivateReq
(%s:%d) First free after a full allocation %d
IBI_CALL_PS_ATTACH_APN_SETTING_ROAM_2
IBI_CLS_POS_CAP_LTE_ECID_FILTER_SUPPORT
IBI_SIM_ACCESS_USIM_TYPE
IBISimFileGetCdmaAuxInfoRspCb
IBI_SMS_BUSY
sim_slot_id_length_t1
IBI_EVS_7_2_Kbps
IBI_RF_ANTENNA_LOCATION_MIDDLE_RIGHT
IBINetIceApStatusRspCb
IBI_CALL_PS_TFT_DIRECTION_BIDIRECTIONAL
IBI_CPS_REJECTED_S_NSSAI_CURR_RA
IBI_MSIM_REMAP_START
IBI_RAT_GSM
IBI_STW_HEATMAP_VISIBILITY_LEVEL_MEDIUM
p_at_payload_t2
CsiIdcTestModeCmd
gsm_scell_info_t13
CsiTraceModeInitRspCb
remove
IBIEnableVirtualSimReq
IBI_MSIM_SET_DATA_SIM_CAUSE_DATA_PREF_CHANGE
AP_3G_RAT_SWITCH
IBI_SS_LCS_POS_CAP_LTE_MDT_LOCATION_RESPONSE_TIME
t_s_UtaIdcCnvAntBlockPwrLmtPolicyConfig
IBI_FILER_HS_CLIENT_WR_TEST
IBI_NET_SMS_VIA_PS_SIGNALLING_NOT_SUPPORTED
IBI_SIM_SEARCH_RECORD_FF_PATTERN
IBI_STW_DEACTIVATION_REASON_DISABLED_BY_NW_CAUSE_USER_END_OF_SUBSCRIPTION
wifi_bssid_t6
startClient_nl_block_invoke
ARI_RT_WRONG_STATE_E
IBI_CALL_CS_CALL_IS_DISCONNECTED
IBI_NET_BAND_NR_66
deregisterClient
version_t2
IBISmsSendResult
cs_error_t5
IBIStwV2ActivateReq
IBIMsSsLcsMtlrRejectIndParam
IBI_CALL_CS_MS_PS_REJECT
IBI_NET_DC_IMS_REGISTRATION_STATE_RETRY
eps_qos_t7
csg_info_valid_t4
SearchInterval_t4
IBIRfPortMap
IBI_CALL_CS_ONLY_RESTRICTED_DIGITAL
IBI_SIP_EVENT_SESSION_SRVCC_EV
skip_barring_mmtel_video_t6
IBI_SIM_TK_PROACTIVE_CAUSE_MULTIPLE_CARD_COMMANDS_ERROR
IBI_SS_LCS_POS_CAP_GNSS_SYSTEM_GSM_BDS_SUPPORT
umts_ncell_info_valid_t15
setMaxOutstanding
call_barring_new_pwd_t7
IBI_CALL_CS_MS_DIRECTED_SIGCONN_RE_ESTABLISHMENT
IBI_CALL_CS_MS_RELEASE_OOSA
sdes_item_type_t6
file_count_t4
ARI_ATTR_LPM_COMMIT
IBI_CALL_CS_MPARTY_SPLIT_REJECTED
IBI_NET_BAND_NR_39
IBICallPsIdleConnFiltersConfigRspCb
bMSISDN_t96
cdma_evdo_ncell_info_t41
IBI_SIM_UNKNOWN_FILE
IBICallCsJoinCallsReq
IBINetApBatterySaverModeType
IBIStwV2FileSignature
IBI_SIM_TK_TONE_RINGING_TONE
CsiIdcUartType4StatsConfigRspCb
PDP_ContextList_t3
fuzzed_location_t5
IBI_CALL_PS_RESULT_CODE_N1_MODE_NOT_ALLOWED
IBI_SIM_ACCESS_SIM_STATE_RESTORE_MODE
IBINetBandSettingsExt
feature_status_t3
PAIRING_CMD_GET_ENONCE
address_t15
CsiSecGetRandomNumReq
IBI_CALL_CS_FEAT_DISABLE
IBI_SMS_RESOURCE_CONFLICT
isMeasInCdmaTime_t9
utran_rel_t5
wci2_msg7_t9
IBI_NET_BAND_CDMA_19
test_cmd_len_t3
09_net_cell
setGroupWakeable_nl
IBI_SMS_TP_FCS_CMD_NOT_ACTIONED
IBI_STW_TRAFFIC_DATA_RATE_2PT5KBPS
media_session_id_t3
memory_status_t1
IBIOgrsActivationType
IBI_NET_DC_IMS_SERVICE_TYPE_VOICE_SMS
chv_attempts_t20
IBINetDcVoiceOverNRCapability
preferred_nssai_list_t3
IBI_LQM_TRAFFICCLASS_AP_ENABLE
IBI_NET_BAND_SELECTION_MODE_CURRENT_CONFIGURATION
hplmn_or_ehplmn_t3
IBI_NET_DC_IMS_SESSION_STOPPED
band_t3
clearCancelled
CsiIceAudInterfaceInfoIndCb
IBI_SS_GSM_ERROR_FACILITY_NOT_SUBSCRIBED
IBI_OGRS_DISCOVERY_STATUS_MAX
is_enabled_t4
CsiSecRFSelfTestCompletionIndCb
lte_scell_info_r15_v2_t57
IBIRemotePeerConfiguration_t
health_activity_status_t4
UtaCpsSetSvnReqParam
IBIMsLpMeasurePositionAssistanceRequestRsp
IBICallPsFlushDataRspCb
IBICallPsCriticalPsSessionStatus
IBINetRadioConnectionStateIndCb
t_s_UtaIdcCamAntBlockPwrLmtPolicyConfigBundleV3
existing_pdu_session_id_t3
audio_channel_mode_t13
IBI_LQM_NR_FR2_RECOMMENDATION
IBI_CALL_PS_VOIP_CALL_STATE_UNKNOWN
registerEvents_block_invoke_2
IBI_SMS_INVALID_REFERENCE_VALUE
CsiIceAudToneConfig
IBICommonReturnCodes
IBI_CALL_CS_VOID_CAUSE
IBI_NET_REGISTRATION_REJECT_CAUSE_REJ_BY_NETWORK
IBI_SIM_HW_EVENT_INOUT_EDGE_DETECT_IN
tac_v1_t19
stopClient_nl
IBI_SMS_ERROR_CAUSE_SMS_SERVICE_NOT_AVAILABLE
IBI_CALL_CS_DUAL_SIM_RADIO_CONFLICT
IBI_SIP_EVENT_OUTGOING_SESSION
IBI_SIP_EVENT_SESSION_FAILIRE_TIMEOUT
IBI_SS_OC_NW_USSD_NTF
IBIMsLpGpsDgpsCorrectionsIndCb
cdma1x_radio_signal_report_config_t6
message_mode_t17
IBI_CALL_PS_RESULT_CODE_DNN_NOT_SUPPORTED_OR_SUBSCRIBED_IN_SLICE
IBI_SEC_TEMP_ID_UPDATED
IBI_SS_MM_CONGESTION
IBIImsMEResult
IBI_CALL_CS_MS_NOT_REGISTERED
IBI_EVS_WB
nInstance_t3
ARI_ATTR_WAKE_AP
CsiModeSetIndParam
IBI_OGRS_SYSTEM_STATUS_Resumed
IBI_SIM_PB_RESULT_ERROR_USIM_PB_NOT_SELECTED
override_concurrency_t9
IBI_XO_MODE_CONNECTED
IBIStwV2ProtocolMode
IBI_NET_BAND_LTE_65
IBIMsLpGanssAdditionalIonosphericModelIndCb
modePref_t3
CsiIceAudSetI2SRespCb
IBI_CALL_PS_SM_CAUSE_ACCEPT_TYPE_IPV4_ONLY_ALLOWED
IBI_NET_BAND_NR_94
IBI_NET_CELL_EVENT_SLOC_OOS
IBI_NET_ERROR_WIRELINE_ACCESS_AREA_NOT_ALLOWED
IBI_STW_SUSPEND_REASON_GPS
SIM_MAP_FAILURE_CARD_RESET_UNSUCCESSFUL
IBI_SMS_ABNORMAL_RELEASE_CHANNEL_UNACCEPTABLE
IBISimEfAccessErrorCause
registerAsClient
rx_diversity_t1
IBI_CALL_CS_ERROR_CAUSE_CDMA_TC_RELEASE_MS
IBI_SIP_MSG_SUBSCRIBE
rtcp_profile_t12
IBICallCsVoimsANBRDirection
eid_t4
IBI_NET_EVDO_REV_A
CsiIpcCtrlPathTestSrcRspCb
cdma1x_scell_info_valid_t30
next_valid_rec_number_t5
IBIVinylStatusReq
IBI_CALL_CS_CLIENT_REJECTED
IBI_CALL_CS_UNKNOWN_SUBSCRIBER
IBIMSimOperModeStatus
IBI_SMS_LOWER_LAYER_FAILURE
IBI_SS_GSM_ERROR_UNKNOWN_ERROR
IBICallPsDataStallInfoRsbCb
IBINetGetCellInfoIndCb
IBI_SIM_PB_LOCATION_MSISDN_PHONEBOOK
IBI_SMS_MS_RRC_CONN_ESTABLISHMENT_FAILURE
IBI_CALL_CS_ALL_CALLS
ari
IBI_NET_BAND_GSM900_P
IBI_STW_DEACTIVATION_REASON_OTHER
ip_addr_t5
IBINetRegistrationMode
IBI_LQM_MAX
IBI_LP_SERVING
AriToken
deprecated_tlv2_t2
IBICallPsDataBearerInfoIndCb
on_non3gpp_access_t15
IBIStwInitiateRegistrationReq
IBI_CLS_POS_CAP_GNSS_MODE_LTE_MS_STANDALONE_SUPPORT
IBI_NET_BAND_UMTS_TDD_F
gsm_band_t14
t_s_UtaIdcCellConfigV3
IBI_CALL_PS_RESULT_CODE_PDP_CONTEXT_WITHOUT_TFT_ALREADY_ACTIVATED
IBI_CALL_PS_RESULT_CODE_SEMANTIC_ERRORS_IN_PACKET_FILTER
IBIVinylPrlActSimFile
IBI_LP_GNSS_TIME_ID_BDS
(%s:%d) Invalid response size %lu\n
IBINvmSnapshotReq
IBIVinylPartialActiveMetaDataRspCb
IBI_CALL_CS_REJECTED_BY_NETWORK
IBI_CALL_PS_RESULT_CODE_SYNTACTICAL_ERROR_IN_THE_TFT_OPERATION
nr_list_t8
trigger_id_t12
IBICallPsIdleConnFiltersConfigReq
IndicationReregistrationActor
IBIOtaspStatus
ARI_NO_MORE_MEMORY_E
IBIEmbmsServiceLossIndCb
IBI_SIM_TK_PROACTIVE_CAUSE_INVALID_PROACTIVE_CAUSE
IBI_SMS_REEST_FAILURE
IBISimSearchRecordInfo
IBI_LQM_LINK_STATE
IBI_SIM_MSG_TAG_TYPE_MT_READ
IBI_SIP_EVENT_INCOMING_SESSION_EST
(%s:%d) Filer initiator response detected but filer ctx 0x%x is already in flight!
(%s:%d) Transferring indication cid marked as 0x%x back to cid 0x%x
IBITxAntennaLocationReportInd
IBIIdcRTConfigEx
diag_cmd_rsp_t5
IBI_NET_REGISTRATION_STATUS_NORMAL_SERVICE
pdp_req_type_t33
sms_service_t3
IBIAlignmentCheckRspCb
CsiIdcRTUartActivityStatsConfigRspCb
IBI_CALL_PS_LOOPBACK_TEST_MODE_B
IBIPeriodicCounterBufferAllIndCb
IBISipMsgInjectToCpIMSTraceRsbCb
cdma1x_ncell_info_len_t24
samplerate_t1
IBI_SIM_ACCESS_APP_TYPE_RUIM
IBIXccLtlRspCb
IBI_CALL_PS_MEAN_THROUGHPUT_20K
IBI_NET_BAND_LTE_11
IBINetDcSsacBarringInfoResult
ascii_symbol_t1
IBIP2PMsgPushReq
IBI_NET_NW_EMERGENCY_FALLBACK_SUPPORTED_EUTRA_5GCN
num_mbim_filters_t7
registerEvents_block_invoke
IBINetDcUacAccessCheckReq
CsiIceSarReq
iccid_t3
IBI_VINYL_TAPE_CMD_DELETE_PROFILE
lte_scell_info_ext_t42
FactorySetNvItemsSettingReq
IBI_CALL_CS_CALL_WAITING_NEW_CALL
IBI_NET_BAND_UMTS_XIII
IBI_SIM_INVALID_ADDRESS
IBI_SS_GSM_ERROR_NETWORK_OUT_OF_ORDER
IBINetCellInfoIndParam
CsiIceCaEnableReq
slot_id_t3
IBI_CALL_PS_SSC_MODE_2
IBINetDcImsSignallingType
0x%03x
IBICallPsBandwidthEstimationInfo_V2
IBINetEmergencySearchModePref
IBINetCdmaEvdoCellInfoParam
send_dtmf_t6
ue_policy_classmark_t10
IBI_CALL_CS_MS_SEMANTICALLY_INCORRECT_MSG
IBI_NET_USER_CAUSE_ENABLE_SERVICE
IBICallCsGetTtyDeviceModeReq_V2
IBIStwSecConfigRspCb
IBI_MSIM_REMAP_COMPLETE
IBI_SS_GSM_ERROR_RESOURCES_UNAVAILABLE
DeregisterClient
cdma_preferred_rat_settings_t7
i20@?0*8I16
IBI_SIM_TK_PROACTIVE_CAUSE_LAUNCH_BROWSER_BEARER_UNAVAILABLE
IBI_SS_GSM_ERROR_INTERWORKING
tcp_mitigation_info_t9
(%s:%d) Clearing transaction manager for cid 0x%x
IBICallCsJoinCallsRspCb
sim_op_t3
IBI_SIM_PRIMARY_CARD
IBI_SIM_TK_PROACTIVE_CAUSE_LAUNCH_BROWSER_BROWSER_UNAVAILABLE
IBI_SS_MM_IMEI_NOT_ACCEPTED
IBICallPsDnsRawPubKey
gsm_ncell_info_valid_t18
no_of_session_t3
usim_pb_location_t3
ARI_TOO_MANY_REQS_E
IBI_CDMA_LANGUAGE_POLISH
IBI_NET_BAND_NR_52
IBI_SIM_TK_PROACTIVE_CAUSE_ACTION_IN_CONTRADICTION_WITH_THE_CURRENT_TIMER_STATE
IBI_CALL_CS_REESTABLISHMENT_COMPLETED
IBI_SIM_ACCESS_SIM_STATE_NOT_DETECTED
IBI_SIM_TK_PROACTIVE_CAUSE_BEARER_INDEPENDENT_PROTOCOL_ERROR_REQUESTED_BUFFER_SIZE_NOT_AVAILABLE
IBI_SIP_MSG_CANCEL
IBI_SS_USSD_IT_MO_DATA
UtaIdcRTSetScanFreqReqV3
is_sat_system_t32
CsiSecGetRandomNumRspCb
IBILpDiscardReason
IBICallPsStopDataCallReason
IBI_CALL_PS_CRITICAL_PS_SESSION_FAILED
IBI_NET_FD_DISCARD_CAUSE_OR_LOW_PRIO
IBI_SIM_TK_COMMAND_TYPE_INVALID_COMMAND
iccid_t2
IBI_CALL_PS_AV_STREAMING_ONGOING
IBI_CALL_PS_STREAMING_ENHANCED_BUFFERING_STARTED
IBI_NET_AP_CARPLAY_TYPE_INVALID
IBI_SIM_RES_TYPE_ERROR_CAUSE_NONE
IBIQoEQueryRspCb
bDnsIPv4_t45
octets_sent_t9
IBI_SIM_TRAY_ABSENT
(%s:%d) Setting indication %s to wake AP failed via ctx 0x%x (Received NACK with reason %s)
is_last_auth_msg_t4
p_at_ext_payload_t1
IBIEmbmsIntraFreqInfo
IBICpmsPowermWInd
UtaIdcSetCriticalCarrierConfigReqV2
numValidConfiguration_t2
IBI_CALL_CS_BURST_DTMF_WIDTH_200MS
(%s:%d) REQ(%s) not allowed during stall [%s]
IBISsAddressData
IBI_CALL_CS_MPARTY_SPLIT_STARTED
IBI_NET_CONFIG_ERR_VOLTE_CALL_ACTIVE
IBI_NET_DC_IMS_STATUS_NOT_REGISTERED
IBI_NET_DC_IMS_RE_REGISTRATION
calibration_status_t5
IBILteCellInfoR15
CsiIdcGetCellConfigRspCb
(%s:%d) Sending reply for cid 0x%x event %s
SendInternal
IBI_SS_LCS_SHAPE_TYPE_POLYGON
overRidingMethodType_t7
UtaIdcSetRTFeatureSpmiRxRspCbV2
category_fields_t9
qos_3g_t35
IBIStwV2ResumeReq
is_reset_sim_t3
IBI_CALL_PS_IP_TYPE_V6
IBI_NET_BAND_NR_12
ip_type_t5
wifi_call_active_t8
rplmn_freq_info_t10
IBI_SIM_APDU_CMD_MORE_DATA_EXPECTED
envelope_rsp_t3
IBI_CALL_CS_MPARTY_IS_ACTIVE
iccid_t32
max >= INVALID_RES_ID
t_s_UtaIdcCellConfigV4
network_plmn_name_t4
ARI_INVALID_MSG_BUFF_E
mid_range_list_t4
IBI_CALL_CS_SS_INCOMPATIBILITY
IBI_NET_DC_IMS_SERVICE_TYPE_VOICE
setGroupWakeable_nl_block_invoke_2
TraceSetBasebandAnomalyDetectionConfigReq
screen_lock_status_t6
IBI_NET_PLMN_NAME_INFO_RESULT_FAILURE_REQ_IN_PROGRESS
IBISetFilterRspCb
CsiIceGetFactoryDebugEnabledReq
 MSG(
IBI_CDMA_LANGUAGE_HUNGARIAN
IBI_CDMA_SMS_ERR_CAUSE_INV_TELESERVICE_ID
IBI_NET_NW_EMERGENCY_FALLBACK_SUPPORTED_NR_5GCN
IBISimTrayStatusRspCb
ecc_list_sim_length_t3
IBISimTkProactiveCmdSetupCall
IBI_CALL_CS_CALL_RETRIEVE_STARTED
IBI_CDMA_SMS_ERR_CAUSE_DEST_NOT_AT_ADDR
IBI_SS_NET_ERROR_NUMBER_OF_PW_ATTEMPTS_VIOLATION
IBI_SS_OC_MO_USSD_DATA
IBICallPsLoopbackTestModeStatusRsp
IBICallPsServiceTypeUpdateRspCb
IBICallCsVoimsCallStatusParam
speaker_state_t1
IBI_SS_NET_ERROR_ERROR_STATUS
IBINetSignalScellInfo_V1
IBINetDcImsGetImsRegStatusInfoReq
IBICallCsBurstDtmfRspCb
IBI_CALL_CS_ERROR_CAUSE_CDMA_TC_RELEASE_POWER_DOWN_BY_USER
IBI_NET_EMERGENCY_SEARCH_MODE_PS_OVER_CS
IBI_NET_RAT_MODE_NR_DISABLE_NSA
(%s:%d) stalling clients
IBISendApacsDataRspCb
IBI_CALL_PS_CRITICAL_PS_SESSION_FINISHED
IBI_IMS_ME_DTMF_DIGIT_CODE_0
sendNotifyAck
CsiIceAudDisableAudioRespCb
IBI_PRI_STATUS_WRITE_NOT_ALLOWED_BY_NW_POLICE
IBICallPsConfiguredMaxBw
CheckRestoreCompletedReq
(%s:%d) Multicast[%u] indication %s to cid(%d) q(%s)
CsiIceGetArfcnLockRspCb
UtaIdcCellConfigEventIndCbV2
IBI_NET_DC_IMS_REGISTRATION_STATE_SUCCESSFUL
IBI_STW_V2_DEVICE_PHONE
commonAlmanac_t2
(%s:%d) client 0x%x did not cancelTrx(0x%x) in %dms.  Likely client queue is stuck or stalled!
IBICallCsVoimsProvideRTPSessionStatusRspCb
error_code_t4
UtaInt8
IBI_SMS_TP_INVALID_USER_DATA_LENGTH
IBI_STW_CHANNEL_TYPE_UCAST_PREAMBLE
almanac_t4
IBIEmbmsGetSAIListReq
BB_info_t6
is_serving_rat_tdd_t3
IBI_NET_BAND_LTE_18
nr_scell_info_v2_t59
ALL_READY
CsiBspDebugJtagModeReq
IBI_CALL_CS_RECOVERY_ON_TIMER_EXPIRY
IBI_NET_UMTS_PWR_CLASS_1
IBI_SMS_ABORT_BY_NETWORK
IBI_SS_NET_ERROR_UNKNOWN_SUBSCRIBER
IBI_VINYL_SIM_CFG_NO_HW
 bytes][READ]
is_nsa_disable_t6
IBI_NET_NW_UP_CIOT_OPTIMIZATION_NA
IBI_SS_NET_ERROR_INTERNAL_SS_TIME_OUT
IBINetSetECBMReq
IBICpsCellularPowerReportInd
IBI_CPS_REJECTED_S_NSSAI_NOT_PRESENT
IBI_FILER_HS_COMPRESSION_LZFSE
IBI_SIM_PIN1_APP3_KEY
IBISimFileUpdateBinReqData
bPcscfIPv6_t35
safeReleaseTrx_nl
CsiPowSleepSetSleepBlockerReq
CsiModeSetRespCb
IBI_CALL_CS_BURST_DTMF_WIDTH_95MS
IBI_SIM_PIN2_APP2_KEY
IBISimAccessAppInfoParam
cdma1x_scell_info_len_t31
(
IBI_CALL_PS_SYMPTOMS_INFO_MESSAGE_TYPE_DEFAULT
IBI_SMS_TP_FCS_TP_VPF_NOT_SUPPORTED
IBIMsLpGpsUtcModelIndCb
IBIMsLpGpsRealTimeIntegrityIndCb
FactoryGetNvItemsSettingReq
interface_type_t1
IBI_STW_V2_CAUSE_INVALID_MSG_IDENTIFIER
data_read_t8
signature_t4
play_tone_t9
band_settings_3gpp_ext_t10
IBI_CALL_CS_VOIMS_MMTEL_SESSION_ATTEMPTED
IBILteCellInfoT
IBISsUssdType
IBICallCsEmergencyCallIntermediateStatusIndCb
IBI_NET_EM_CALL_TYPE_T911
IBI_SIM_CMD_MORE_DATA_AVAILABLE
IBI_SS_NET_REJECT_RESOURCE_LIMITATION
read_rplmn_param_t7
glonassAlmanacElementCount_t3
navDataGlonassCount_t3
UserID_t2
IBIStwGetServiceInfoRspCb
IBI_CALL_PS_LLC_SAPI_SAPI_11
IBI_CALL_PS_RESULT_CODE_REQUEST_SERVICE_OPTION_NOT_AUTHORIZED_IN_THIS_PLMN
IBICallPsLteAttachIndCb
lqm_fp_t4
IBI_SIM_ADM_PIN_KEY
IBI_SIM_TK_SETUP_CALL_DISCONNECT_ALL_OTHER_CALLS_WITH_REDIAL
IBI_VINYL_TAPE_CMD_SET_DEFAULT_DP_ADDRESS
networkType_t3
direction_t3
service_type_t4
IBINetRatNRStatusReq
IBI_CALL_PS_DELAY_CLASS_SUBSCRIBED
IBI_CPS_FEATURE_STATUS_DISABLED
IBI_NET_BAND_LTE_87
IBI_NET_NW_IWK_WITHOUT_N26_NOT_SUPPORTED
IBISmsSendMoreMessagesStatus
client_id_t1
IBI_CALL_CS_MOC_CALL_SETUP
IBI_NET_BAND_NR_25
IBI_SIM_APPLICATION_SELECT_PART_NAME_LAST
IBISimFileReadBinaryReq
SetRTEventHandler
IBICallPsVoIPCallInfo
(%s:%d) Received tlv with g(%d) m(0x%03x) tid(%d) len(%d) > exp(%zu), ignored
rtcp_profile_t10
(clientId == NULL) || (name == NULL) || (jobQueue == NULL)
(%s:%d) failed to flush stalled requests for cid 0x%x
IBIXccClockControlReqParams
IBI_CALL_PS_RESULT_CODE_IMPLICITLY_DETACHED
IBI_OGRS_DISCOVERY_STATUS_LinkFailure
IBI_OGRS_RELAY_LIKELIHOOD_Level2
latitude_t5
CsiIdcSetWifiStatusReq
plmn_w_ac_t_t10
IBI_CALL_PS_AUTHENTICATION_TYPE_CHAP
IBI_CALL_PS_SUSPEND_CAUSE_FLOW_CONTROL
IBI_SIM_PIN_ACTIVITY_DUMMY_VERIFY
(%s:%d) unknown notification %u
earfcn_t4
gsm_rel_t4
IBISimInfoStruct
IBI_NET_CONFIG_ERR_FEATURE_NOT_SUPPORTED
IBI_NET_NW_MAX_15_BEARER_NOT_SUPPORTED
IBI_RF_ANTENNA_LOCATION_MIDDLE_LEFT
(%s:%d) Successfully set wakeable attribute(s) with status %d via request GMID 0x%x
IBINetRegistrationInfoIndCb
CsiBspStateGetReq
CsiMsCpsReadMeidRspCb
IBI_IMS_ME_RTCP_SOURCE_REMOTE
IBI_SIM_ACCESS_APP_TYPE_ISIM
IBICallPsStatusInd
umts_tdd_band_status_t6
IBI_CALL_CS_CDMA_SPC_VALIDATION_FAILED_MAX_ATTEMPTS_NOT_REACHED
IBI_CALL_CS_ERROR_CAUSE_CDMA_CALL_DTMF_REJ_ORDER_ERROR
IBI_CALL_PS_CRITICAL_PS_SESSION_ENDED
IBI_CALL_PS_RESULT_CODE_UNKNOWN_PDP_CONTEXT
IBI_NET_NW_MBMS_NA
IBICallPsLoopbackTestMode
isEUtranValid_t5
IBI_PRI_GRI_STATUS_FILER_REG_ERR
IBISmsIncomingSmsAck
IBI_NET_BAND_NR_16
IBI_NET_NW_MAX_15_BEARER_SUPPORTED
is_always_on_t22
IBI_EVS_128_0_Kbps
IBIOgrsTxDiscardRspCb
IBI_FILER_HS_CLIENT_L1C
IBI_SS_GSM_ERROR_DESTINATION_OUT_OF_ORDER
IBILpPosProtocol
throttling_timer_status_t6
IBINetTimerStatus
is_nsa_disable_t10
IBI_CALL_PS_SOURCE_STATISTICS_DESC_SUBSCRIBED
IBI_CALL_PS_STOP_DATA_CALL_REASON_IPV6_ADDR_REFRESH_FAILURE
IBI_LP_WLAN_ERROR_CAUSE_UNDEFINED
[ERROR]: 
add_compression_header_t6
IBIStwV2ActivateRspCb
IBI_SMS_SAPI3_RELEASE
eps_qos_V1_t39
CsiIceSetTxAntennaRspCb
UtaIdcSetCnvAntBlockPwrLmtConfigRspCbV2
IBI_NET_ERROR_NOT_AUTH_FOR_THIS_CAG_OR_AUTH_FOR_CAG_ONLY
IBI_NET_ERROR_SYNCH_FAILURE
IBI_NET_UAC_SERVICE_TYPE_SMS_IP
UtaIdcSetUsbEnhAntBlockPwrLmtPolicyConfigRspCb
IBI_SS_LCS_SHAPE_TYPE_POINT_UNCERTAIN_ELLIPSE
tuid_t7
IBICpsHealthActivitySwimLocationType
IBI_CALL_CS_ALERTING_CATEGORY_2
IBI_NET_EMERGENCY_SEARCH_MODE_CS_ONLY
IBI_SIM_APDU_CMD_NO_INFO_GIVEN_TYPE2
IBINetGetRegistrationInfoReq
IBI_CALL_PS_PIPE_PARAMS_APPLICABLE_TO_CID
IBI_NET_USER_CAUSE_AIRPLANE_MODE
CsiAwdsGlobalSwitchReq
IBI_MSIM_OPER_MODE_STATUS_FAILURE_UNKNOWN
mo_ims_reg_signalling_t8
tmgi_info_list_length_t3
IBICPMSPowerQueryReq
msgAttrib_t1
AriGroupAttribParam
IBI_VINYL_SUPPORT_UNKNOWN
cmd_type_bitmask_t9
sa_disabled_reason_t9
IBI_LP_POSITION_METHOD_LTE_ECID
isVoNRCapabilityValid_t11
IBI_CALL_PS_PRECEDENCE_CLASS_NORMAL
IBI_CALL_PS_RESULT_CODE_REGISTRATION_IN_PROGRESS
IBI_NC_CFG_REQ_NUTCRACKERENV
IBI_SIM_CMD_MORE_DATA_AVAILABLE_PROACTIVE_CMD_PENDING
IBI_SIM_PB_RESULT_ERROR_UNSUCCESSFUL
IBI_SS_SV_CODE_USSD
IBIPriWriteReq_V3
CsiIceGetManifestStatusResp
(%s:%d) targetSet is empty! This is likely not invoked atomically
IBI_CALL_CS_FACILITY_NOT_SUBSCRIBED
IBI_CALL_CS_VOIMS_MMTEL_SESSION_PREAMBLE
IBI_SIM_APDU_CMD_MEMORY_PROBLEM
IBI_NET_NW_LCS_VIA_CS_NA
IBI_SMS_MS_DETACH
badSatInfo_t4
IBICallPsVoipAppInfoReq
bImCN_t61
STALL4CRASH
IBI_SS_GSM_ERROR_USSD_CHANGED_TO_CALL
sm_cause2_t6
(%s:%d) cancelling host stalled requests and stalling client work queue
t_s_UtaIdcCriticalCarrierConfig
IBI_NET_BAND_NR_70
IBI_SIM_TK_PROACTIVE_CAUSE_COMMAND_PERFORMED_WITH_MODIFICATION
p_at_ext_payload_t2
IBICallCsDisconnectedIndCb
ref_temp_mc_t27
IBI_CALL_CS_CALL_MODIFY_COMPLETED
IBI_CLS_POS_CAP_LCS_NOTIFICATION_MECHANISM_SUPPORT
IBI_SIM_ACCESS_SIM_STATE_CUST_4
NotifyEventCallback
CsiIceBBTxStateIndEnableRspCb
IBI_VINYL_PRLACT_SIM_FILE_IMSI
(%s:%d) cancelling blocked requests for cid 0x%x
IBISimTkProactiveCmdSendDtmf
payload_t4
deregisterAsClient
IBI_NET_BAND_CDMA_16
IBI_NET_BAND_NR_260
bDSMIPv6v4_haar_t16
IBI_CALL_CS_NO_ROUTE
IBIStwEvalFringeCellConditionReq
IBI_CALL_CS_BURST_DTMF_INTERVAL_150MS
IBI_CALL_CS_LONG_TERM_DENIAL
IBI_NET_FD_DISCARD_CAUSE_CALL_RE_EST
a0_t3
gsm_scell_info_t9
CsiIceBspWakeInd
CSI_ICE_IPC_MEM_HOST_WAKE_REASON_INFO
data_roaming_t4
channel_id_t3
verify_data_t10
gold_fw_version_t16
IBI_STW_CAUSE_S4_DATA_MISSING
qos2g_t3
IBISimTkAddress
msg_id_t2
(%s:%d) %s delay(%d) exceeds warning level(%d) 
IBIConfiguredSimInfoIndCb
IBI_LP_IGNORE_AFLT_MEASUREMENT
eCSI_ICE_PS_STATE
IBI_VINYL_ATC_ICCID_NOT_FOUND
skip_barring_mmtel_voice_t7
(%s:%d) Checking for item 0x%x in queue when not stalled! [%s]
UtaIdcSetCnvAntBlockPwrLmtConfigRspCb
IBI_NET_BAND_CDMA_20
CsiSahClearExceptionStoreReq
IBI_CALL_PS_UL_SDU_SCALING_SET
gpsCellTimingWanted_t8
IBI_NET_BAND_NR_53
IBI_SS_GSM_ERROR_NORMAL_CALL_CLEARING
notificationOfLeapSecond_t7
%s
IBI_CALL_PS_NR5G_NEIGHBOR_CELL_UNKNOWN
IBI_NET_ERROR_INVALID_MANDATORY_INFORMATION
IBI_NET_GSM_SERVICE_CIRCUIT_SWITCHED
IBI_SS_LCS_LOC_ESTIMATE_TYPE_INVALID
result_code_t2
channel_mode_t16
coeff_c1_t7
IBI_EVS_16_4_Kbps
IBISimAccessCardTypeInfo
sip_nai_data_t5
(%s:%d) Filer transaction [cid=0x%x, trx=0x%x] appears to have exited too early!  Check if it was cancelled
CsiIdcControlEventReq
IBICallPsSecurityStatusReq
data_stall_detected_t4
IBINetGetCurrCellInfoReq
message_mode_t7
IBIRfSetAntennaPortMappingResp
param_t1
IBI_SMS_TP_FCS_TP_VP_NOT_SUPPORTED
IBIImsMETerminateMediaSessionRspCb
(%s:%d) Unblocking for ctx 0x%x (cur %zu max %u) %s
report_tc_ap_t5
sleep_length_t3
IBI_CALL_CS_BEARER_CAPABILITY_NOT_ALLOWED
registerActor
UtaIdcSetUwbAntBlockPwrLmtConfigReqV2
UtaIdcCellConfig
IBI_CALL_PS_RESULT_CODE_IMSI_UNKNOWN_IN_HLR
IBI_SEC_TEMP_ID_NOT_UPDATED_FOR_LONG_TIME
IBI_SIM_CMD_REF_DATA_NOT_FOUND
bImCN_t11
serv_cell_info_t3
IBI_CALL_CS_NO_USER_RESPONDING
IBI_CALL_CS_MOC_CALL_ALERTED
IBI_STW_CELL_STATUS_POOR
IBISimTkProactiveCmdDisplayText
IBINetCbrsConfigReq
security_param_t5
TrafficClassinfoWithDataStallinfo_t4
(%s:%d) ExitTrx() is deprecated.  Attempt to exit transaction ID 0x%04x.  Ignoring...
IBISimTkConfigureStkCmdReq
carplay_info_t7
IBIOgrsDiscoveryReleaseRspCb
IBI_NET_BAND_NR_255
SIM_CARD_STATUS_PRESENT
IBISimTkProactiveCmdUnknown
service_mode_t16
IBINetPreferredNssaiInfoReq
IBI_NET_EM_CALL_TYPE_NONE
(%s:%d) waiting for registration reply to come back: %s
umts_ncell_info_len_t12
(%s:%d) indicationRegId not set.  Deferring RT registration of %s (%d-0x%x).  Total deferred: %zu
item_id_t4
waking_indicator_t2
IBI_NET_BAND_SELECTION_MODE_AUTOMATIC
unknown
IBIEmbmsInterFreqInfo
t_s_UtaIdcTunerArbitrationConfigV2
IBI_SS_GSM_ERROR_DUAL_SIM_NO_SERVICE
IBI_SS_SV_CODE_UNKOWN
locationInfo_t6
CsiIpcCtrlPathTestUnInitRspCb
IBI_CALL_CS_AUX_STATE_HELD
IBI_SIM_TK_PROACTIVE_CAUSE_COMMAND_NUMBER_NOT_KNOWN_BY_ME
report_nr_fr2_recommendation_t9
DeregIndication_block_invoke
IBI_XO_MODE_INVALID
ClientInboundIndCB_block_invoke
CsiIdcSetWifiStatusRspCb
calling_name_t4
uptime_ms_t1
IBI_IMS_ME_AUDIO_CODEC_TYPE_G711U
IBI_SIM_PIN1_APP2_KEY
IBI_SMS_TP_FCS_CMD_NOT_SUPPORTED
ims_ip_can_t6
IBINetEnabledRatsExt
result_t3
IBI_SIM_TK_PROACTIVE_CAUSE_REFRESH_PERFORMED_WITH_ADDITIONAL_EFS_READ
tds_scell_info_t17
(%s:%d) Failed to deregister actor %s with CID 0x%x
blob_msg_data_t2
LPM_EXIT
IBI_NET_BAND_NR_73
UtaIdcSetSfbmAntBlockPwrLmtPolicyConfigReq
ARI_ATTR_GET
IBI_CALL_CS_REQEUSTED_CIRCUIT_NOT_AVAILABLE
IBI_MODE_CHARGE_ONLY
IBI_SMS_NETWORK_NO_RESOURCE
IBINetConnectionInfoIndCb
(%s:%d) Dropping ind(%d-0x%x): Client(0x%04x) is no longer registered
select_item_V1_t24
IBIEmbmsGetServicesListReq
IBI_SS_LCS_POS_CAP_GNSS_SYSTEM_LTE_GLONASS_SUPPORT
IBI_CDMA_LANGUAGE_KOREAN
IBI_NET_BAND_LTE_27
IBI_NET_PLMN_NAME_INFO_RESULT_SIM_CACHING_ONGOING
Message_t4
(%s:%d) tid(%d) not found under gid(%d) mid(0x%03x)
IBISmsSetMsgWaitIndRspCb
IBI_SIM_PIN_ACTIVITY_VERIFY
IBI_SIM_TK_PROACTIVE_CAUSE_MULTIPLE_CARD_COMMANDS_ERROR_PROTOCOL_NOT_SUPPORTED
IBI_SMS_FAILURE_CAUSE_RSRVCC
IBI_CALL_PS_RESULT_CODE_NOT_REGISTERED
iccid_t4
IBI_CALL_CS_MS_CANNOT_CONNECT_DUE_TO_CALLEE_CIRCUMSTANCE
IBI_CALL_PS_IP_PROTO_ANY
IBICallPsSPKIPin
pdp_req_type_t8
t_s_UtaIdcRTSpmiTxConfig
IBINetSatelliteSystemTrafficInfo
IBI_NET_BAND_LTE_32
IBI_NET_GSM_SERVICE_PACKET_SWITCHED_PREFERRED
IBISimGetSmscAddressReq
Playback_stall_detected_t5
force_t3
CsiCddParamDumpInfo
IBI_SIM_SECONDARY_CARD_3
IBIGetSimMuxCfgRspCb
IBI_CALL_CS_BEARER_CAPABILITY_NOT_AVAILABLE
IBI_NET_DC_BARRING_TIME_S64
IBI_NET_FD_DISCARD_CAUSE_DATA_TCH_H
CancelTrx
CsiAwdsPiiLocConfigRspCb
trace_drop_statistics_t4
IBI_CALL_PS_TFT_DIRECTION_UPLINK
IBI_VINYL_TAPE_CMD_PREPARE_DOWNLOAD
ecc_list_nw_length_t4
IBICallPsDataStallRegReq
encryptionStatusInfo_t5
\n
IBIVinylPrlActSimPin
CsiBspDebugJtagMode
IBIMsLpMeasurePositionMeasurementsRspAckCb
t_s_UtaIdcCellConfig
IBI_EVS_SWB
IBI_SIM_TK_ENVELOPE_TYPE_EVENT_DOWNLOAD_CALL_DISCONNECTED
IBI_SIM_TK_CMD_HANDLER_UNCHANGED
IBI_SS_LCS_POS_CAP_GNSS_VEL_TYPES_SUPPORT
evs_br_t7
CsiMonMemoryStatusRspCb
eCSI_ICE_STATE_ONOFF
cdma_band_settings_t6
IBI_OGRS_FAILURE_CAUSE_NotActivated
IBI_SIM_FCP_SEC_ATTR_REFERENCE
IBI_CALL_CS_ERROR_CAUSE_CDMA_CALL_FLASH_FAIL
IBI_CLS_POS_CAP_GNSS_MODE_GSM_MS_BASED_SUPPORT
unpack
IBIFilerHSReadBBGetSizeRspCb
is_cs_rej_internal_t32
override_registration_timer_in_s_t4
IBI_CLS_POS_CAP_GPS_FTA_MEAS_SUPPORT
AP_2G_RAT_SWITCH
IBI_SS_LCS_LOC_ESTIMATE_TYPE_CANCEL_DEFERRED_LOC
IBILpSessionInfo
region_code_t3
IBI_NET_BAND_UMTS_XXV
locationIndication_t4
sequence_number_t6
IBI_CALL_PS_RESULT_CODE_MBMS_BEARER_CAPABILITIES_INSUFFICIENT_FOR_THE_SERVICE
IBI_IMS_ME_DTMF_DIGIT_CODE_7
t_s_UtaIdcPhycialModePolicyConfig
blob_msg_data_t3
IBI_CALL_CS_MS_LINK_ESTAB_FAILURE
IBI_SMS_MS_L2_CAUSE_NORMAL_CAUSE
CsiIceSecActivationRegisterIndCb
IBI_CALL_CS_MS_NORMAL_EVENT
IBI_NET_BAND_NR_7
IBI_STW_CAUSE_INTERNAL
IBI_STW_UX_CONGESTION_STATUS_NO_CONGESTION
VINYL_RESULT_SIM_MUX_CFG_SUCCESS
IBIImsMECreateRTTMediaSessionReq
IBICallType
post_process_time_ms_t4
IBI_CALL_CS_ABSENT_SUBSCRIBER
IBI_MODE_FORCED_SLEEP
CsiIpcCtrlPathTestDataOpReq
time_in_ms_t2
IBI_FREQ_REPORTING_CONTINEOUS
IBI_IMS_ME_RTT_SESSION_TTY_FULL
environment_t18
tai_t30
adc_gain_ext_t23
IBI_CALL_CS_STRUCTURED_COMPONENT
IBI_CALL_PS_CRITICAL_PS_SESSION_RETRY_ALLOWED
active_rtp_payload_type_ul_t6
IBI_SIM_TK_PROACTIVE_CAUSE_INTERACTION_WITH_CALL_CONTROL_BY_SIM_TEMPORARY_PROBLEM
end_cause_t5
CsiIdcRTGetLinkQualityReportRspCb
IBI_NET_REGISTRATION_STATUS_REGISTRATION_IN_PROGRESS
azimuth_t4
Latency_Target_t5
remote_ip_t10
IBIOgrsInterfaceId
IBI_LP_SEND_AFLT_MEASUREMENT
IBI_IMS_ME_RTCP_SDES_END
IBI_SS_NET_REJECT_UNRECOGNIZED_OPERATION
IBIBbPowerSocSleepStatsRspCb
EndStream_block_invoke
IBISimPbCacheLoadIndCb
IBI_STW_CAUSE_MAX
IBI_CALL_CS_REDIAL_ON_IMS
IBI_SIM_CMD_COND_OF_USE_NOT_SATISFIED
IBI_SIM_ERROR_CAUSE_EMPTY_TRAY
IBI_SIM_UNKNOWN_INSTRUCTION
IBI_XCC_LTL_INFO_TYPE_INITIAL
ARI_TRANSPORT_FAILURE_E
IBI_SIM_PB_RESULT_ERROR_MEM_RETRY_SUCCESS
IBI_STW_V2_PROTOCOL_MODE_PHY_TEST
alfa2_t5
IBICallPsLqmRegisterRspCb
plmn_info_t3
IBI_CPS_FEATURE_STATUS_UNKNOWN
IBI_SMS_PP_ANSI_136_R_DATA
bPcscfIPv4_t69
rtcp_timeout_t18
IBIMsSimSetSmsTagReq
IBIStwV2ResponseParam
IBI_CALL_PS_RADIO_PRIORITY_2
IBINetBandSettings_V1
IBI_SIM_HW_EVENT_INOUT_EDGE_DETECT_OUT
IBI_SS_LCS_GANSS_ID_BDS
IBI_NET_DC_BARRING_FACTOR_P90
methodType_t5
IBICallPsWrmSAInfoRsp
sai_type_t3
nsa_disabled_reason_t11
SOC_SLEEP_SLP_VCXO
IBI_LP_UDRE_SCALE_NO_DATA
IBICallPsUpdateNaiRspCb
IBICallPsLqmTcApEnable
CsiIceAudStatsInfoIndCb
IBIVinylHwIdSimConfigRspCb
 (NOT FOUND IN SDK)
display_text_t10
IBINetRatUnavailableRanDatabaseReq_V2
sim_rsp_data_t6
IBI_SIM_GEN_RES_TYPE_NO_MEM_FOR_RESP
nrOfSats_t8
receive_data_t22
IBISimTkProactiveCmdSendData
bcam_mode_t3
IBIRfRat
IBI_SS_MM_CALL_CANNOT_BE_IDENTIFIED
IBI_TIMESCALE_INVALID
evs_max_redundancy_duration_t27
umts_scell_info_t5
IBISimPbGetLocationRspCb_V1
IBICallPsSuspendIndCb
message_id_t5
(%s:%d) failed to cancel blocked requests for cid 0x%x
EmergencyUserID_t3
IBI_CALL_CS_UNEXPECTED_LINKED_OPERATION
IBINetRadioSignalIndCb
IBINetDcSsacBarringInfoRspCb
ARI_ATTR_LPM
IBICallPsDownlinkBwEstimation
destination_address_t8
IBICallCsAutoAnswerRspCb
t_s_UtaIdcRTSpmiRxConfig
guid_t2
IBI_CALL_CS_SUPPRESS_PHONE_NUMBER
IBI_PRI_GRI_STATUS_WRITE_FAILED_BB_AIRPLANE_TOGGLE
IBICallPsAllowMultiplePDNToSameApnRspCb
TraceSetConfigRspCb
smart_data_mode_t5
deprecated_msg_inherited_tlv2_t2
IBIMsCallCsVoimsProvideMMTelSessionStatusReq
IBI_CALL_CS_MPARTY_REJECTED
IBI_SIM_LINEAR_FIXED_FILE
IBICallPsDataStallRegIndCb
phone_no_t4
IBINetAttachReq_V1
IBI_NET_CELL_NWID_GNB_SW_24R2_NOKIA
timeCellFramesUtran_t10
cdma1x_ncell_info_len_t22
roaming_t8
IBI_CALL_PS_PIPE_TYPE_DL_TR
IBI_FILER_HS_RESULT_ERROR_TRANSFER_TIMEOUT
IBI_SIM_TRAY_PRESENT
VINYL_CAP_NOT_CAPABLE
record_number_t4
IBINetGetCellInfoRespCb
card_presence_t2
IBI_VINYL_PRLACT_GET_IDENTITY_IMSI_BASED
IBICallPsCellularDataInterfaceInfoReq
UtaIdcSetUwbAntBlockPwrLmtConfigRspCbV2
IBISimPbWriteRecRspCb
IBICpsGetFeatureStatusReq
IBI_CALL_PS_RESULT_CODE_SYNCH_FAILURE
com.apple.commcenter.ari.rt.xpc
(%s:%d) Blocking for cid 0x%x (cur %zu max %u blocked %zu) %s
payload_t6
IBI_SS_LCS_VELOCITY_TYPE_HORIZONTAL_WITH_VERTICAL_VELOCITY_AND_UNCERTAINTY
session_key_t5
IBISmsDownloadData
msg_wait_info_t2
is_sat_entitled_app_in_fgrnd_t3
IBI_RF_ANTENNA_LOCATION_BOTTOM_RIGHT
ecc_category_t5
IBI_NET_BAND_NR_72
IBI_SIM_TK_ENVELOPE_TYPE_EVENT_DOWNLOAD_IMS_REGISTRATION
AriCid
proactive_cause_t2
wnlsf_t6
IBINetTac
IBISimGenPinRspCb
mute_status_t1
delay_ms_t4
MsgType_t4
Periodicity_t5
IBI_NET_UAC_CHECK_RESULT_ACCESS_UNKNOWN
app_id_t4
bIPv4Mtu_t73
(%s:%d) flushing host
CsiBspNvmGroupEnumListReq
CsiIceGetAntennaStateReq
IBI_CALL_CS_SIM_STATUS_FAILURE
IBI_STW_V2_CAUSE_S4_DATA_MISSING
CsiIpcCtrlPathTestSrcCfgReq
gsm_ncell_info_len_t12
GetInstance().rtProxy == NULL
embms_service_support_t2
IBINetRatUnavailableRanDatabaseReq
ik_available_t12
IBI_CALL_CS_DESIGNATED_CALL
IBI_CALL_PS_SUSPEND_CAUSE_ROUTING_AREA_UPDATE
IBI_NET_BAND_NR_257
deprecated_inherited_tlv2_t2
), for client(
IBIFilerHSSessionFiles
IBINetDcIPCan
IBI_SIM_APDU_CMD_SECURE_MESSAGING_NOT_SUPPORTED
IBI_SIM_NEVER
CsiIceProvisionPubkeyType
t_s_UtaIdcSfbmAntBlockPwrLmtPolicyConfigV2
IBINetNrRoamingConfig
card_selector_t2
IBILteNeighborCellInfoV1T
rec_num_t5
IBI_CLS_POS_CAP_GNSS_MODE_GSM_MS_STANDALONE_SUPPORT
variable_id_t1
active_profile_t2
ca_enable_t2
UtaIdcSetTxBlankingConfigRspCb
IBINetIceSingleShotFdReq
IBI_SIM_USIM_ENH_SEARCH_AFTER_FIRST_OCCURENCE_FORWARD_FROM_NEXT_REC
IBIPDP_ContextList_t
IBI_CALL_CS_MS_UTRAN_CONFIGURATION_UNKNOWN
IBI_CALL_PS_RESULT_CODE_ERR_UNSPECIFIED
IBI_CALL_PS_RESULT_CODE_N_REG_REQ
IBI_CBS_CAUSE_CONFIG_NOT_CONFIGURED
IBI_XO_STATE_INVALID
CsiIceSecActivationTicketSetReq
CsiIpcCtrlPathTestSrcCfgReqParams
IBICallCsExtEmergencyNumber
slot_id_t2
IBI_CALL_CS_MS_PAGING_PENDING
IBI_OTASP_STATUS_SSD_UPDATED
IBI_SIM_PB_RESULT_ERROR_MEMORY_ERROR
IBI_SMS_ABNORMAL_RELEASE_TIMER_EXPIRED
IBI_XO_STATE_TD_SCDMA
IBINetSignalStrength
num_of_mimo_layers_t5
IBICpsConfigureCellularPowerReportRsp
IBI_NET_AP_SCREEN_STATUS_DIM
IBI_SMS_TP_FCS_SC_BUSY
IBIImsMEMediaDirection
codecs_t16
files_t2
NumPDP_Contexts_t2
IBI_SIM_TECHNICAL_PROBLEM
smsc_add_present_t2
IBISsOperationCode
IBI_CALL_PS_TRAFFIC_PRIORITY_3
hacktivation_state_t6
IBIStwQueryReq
CsiModeGetRspCb
IBISimGenPinReqChangeData
IBI_CALL_PS_RESULT_CODE_CONTROL_BY_SIM_REJECT
IBI_CALL_PS_SDU_ERROR_RATIO_SUBSCRIBED
IBI_ERROR_OUT_OF_HANDLES
(%s:%d) Updating handler CID (0x%x -> 0x%x) for %s
IBINetRatModeStatusReq
map_t3
IBI_OGRS_MASTER_LIKELIHOOD_Level2
ecc_list_sim_t3
audioVideoAppType_t7
IBICallPsWrmSdmInfoRsp_V2
IBI_CALL_CS_ATC_FCLASS_NOT_SPEECH
IBI_IMS_ME_DTMF_DIGIT_CODE_1
IBI_NET_ERROR_IMPLICITLY_DETACHED
IBI_XCC_IND_TYPE_XO_SYNC_STATUS
cdma_hrpd_rel_t7
IBI_CALL_PS_RESULT_CODE_ERR_CONFIG_FAILURE
IBI_NET_FD_DISCARD_CAUSE_REGISTRATION
IBI_SIM_APDU_CMD_SUCCESS_DATA_TRANSFER_ONGOING
IBI_SS_LCS_POS_CAP_LTE_MDT_LOCATION_AGE_LIMIT
v12@?0B8
buf_index_t1
spc_code_t4
IBI_NET_SERVING_CELL_TYPE_PCELL
IBINetRadioConnectionStateRespCb
ext_ecc_list_t7
cpms_power_budget_t1
IBI_CALL_PS_SERVICE_TYPE_IMS
IBI_SIM_TK_TONE_CALL_WAITING_TONE
IBICallPsBreadButterModeReq
codecs_length_t22
IBIXccClockIndCb
matching_id_t4
IBI_LP_GNSS_TO_ID_GALILEO
client_cookie_t3
IBI_LP_MULTI_PATH_MEDIUM
IBI_SIP_MSG_NA
IBI_STW_V2_CAUSE_DEACTIVATION_IN_PROGRESS
IBICallPsImsTestModeReq
ARI_MSG_PARAM_INIT_FAILED_E
IBI_IMS_ME_DTMF_DIGIT_CODE_9
tac_t16
IBICallCsVoimsMMTelSessionStatus
src_dst_mask_t1
IBI_NET_BAND_GSM_T_GSM410
IBI_LP_GANSS_ID_GALILEO
IBILpGanssLocationInfo
IBICallPsModifyIndCb
CsiTraceProfileInitReq
IBI_NET_FD_DISCARD_CAUSE_NW_DEACT
IBIPriWriteReq_V2
dl_thrpt_est_t3
minimum_epoch_t11
(%s:%d) No deferred indication registrations
IBISimTkProactiveCmdType
IBIEmbmsSetInterestedTMGIListReq
csg_id_t5
IBI_NET_NETWORK_OP_MODE_I
apdu_t9
setup_alpha_id_t10
IBISimPbGetMetaInformationReq_V1
IBISimPbReadRecRspCb
coeff_c5_t3
IBI_NET_ERROR_CS_DOMAIN_NOT_AVAILABLE
prl_version_t9
buf_t3
t_s_UtaIdcRTSpmiTxConfigV2
IBI_CALL_PS_IP_TYPE_V4_PDN
IBI_NET_BAND_CDMA_14
IBI_STW_DEACTIVATION_REASON_DISABLED_BY_NW
IBI_VINYL_PRLACT_GET_IDENTITY_NSI_BASED
CsiIdcControlEventRspCb
tethering_status_t4
IBI_SS_NET_REJECT_INITIATING_RELEASE
IBISetEmergencySessionStateReq
bit_rate_count_t11
uart_msg_counting_report_valid_t3
upsi_list_t6
IBI_NET_BAND_NR_20
QoE_RESULT_FAILURE
IBISimTrayStatusReq
IBI_SIP_CALL_TYPE_NA
bandwidthEstimationInfoV2_t6
cdma_evdo_ncell_info_len_t26
(%s:%d) Baseband is ready by the time we pushed indications; register them right away
IBI_SMS_SEND_MORE_MESSAGES_STATUS_DISABLE
IBI_SMS_MS_HANDOVER
cb_name_t5
umts_list_t4
device_samplerate_t1
IBI_LP_UDRE_SCALE_0_2
IBI_LP_GNSS_TO_ID_INVALID
IBI_SIM_APDU_CMD_SUCCESS
cellular_search_enabled_t8
device_type_t6
target_fm_id_t6
IBI_LP_DISCARDED_POS_MSG_TYPE_CAPABILITY_REQ
IBI_RAT_HYBRID_1xEVDO
cdma1x_list_t6
setup_eventlist_t3
IBICallCsVoimsRetryCause
IBIVinylSecureAkaRspCb
fusing_state_t2
alpha1_t3
gsm_scell_info_t11
lte_radio_signal_report_config_t5
CsiSahGetDebugLogRspCb
uid_t4
IBI_SIM_RES_TYPE_NO_MEM_FOR_RESP
ind_param_t1
IBI_CALL_CS_TTY_DEVICE_MODE_VCO
IBI_SMS_PP_NORMAL
IBI_SS_LCS_GANSS_ID_GALILEO
earfcn_list_t4
IBI_SIP_EVENT_INCOMING_SESSION_REFER
IBI_VINYL_ATC_OP_DISABLE_PROFILE
report_transfer_time_t6
IBI_CALL_CS_EMERGENCY_CALL
IBI_SMS_IE_NON_EXISTENT
IBILteNeighborCellInfoT
current_rac_t10
IBI_CALL_PS_DELAY_CLASS_1
IBI_NET_BAND_LTE_74
IBIEmbmsSetInterestedSAIFreqRspCb
eCSI_ICE_BSP_ENABLE
IBINetIqCaptureStartReq
responseType_t4
posProtocol_t12
IBICallPsDataStallInfoReq
cookie_t8
min_packetization_interval_t9
ue_policy_err_length_t7
IBI_CALL_CS_SRVCC_CALL_STATE_ACTIVE_U10
IBI_EMERGENCY_HYSTERESIS_STATE_STOP
IBI_OGRS_PDP_DEACTIVATION_CAUSE_RequetedByAP
IBI_SS_LCS_POS_CAP_CP_POSITIONING_SUPPORT
(%s:%d) Mandatory TLV id(%d) not present for msg (%s). Mark this msg invalid
service_priority_t5
IBI_PRI_GRI_STATUS_WRITE_FAILED_BB_REBOOT_REQD
ganssAddUtcModelSet_t3
privacy_level_t6
msg_data_t3
IBI_NET_EM_CALL_TYPE_NORMAL_SETUP_EM_CALL
IBIPriWriteStatusIndCb_V2
IBISimFileUpdateBinaryRspCb
IBIImsTestReqType
on_duration_t6
IBIOgrsInterfaceStopReq
IBI_CALL_CS_ECT_STARTED
profile_class_slot1_t37
soc_sleep_stats_t3
(%s:%d) Lower free range merged %d
IBI_CALL_PS_RELIABILITY_CLASS_2
IBI_CALL_PS_RESULT_CODE_MESSAGE_TYPE_NOT_COMPATIBLE_WITH_THE_PROTOCOL_STATE
pf_list_v2_t42
(%s:%d) Already tracking 0x%x.  Likely due to reuse of transaction ID.
checksum_t4
IBI_CELL_INVALID_INFO
IBI_SMS_TP_PENDING_MO_SMS
search_offset_t9
call_error_cause_t5
IBI_SIM_PB_RESULT_ERROR_CONTRADICT_WITH_CHV_STATE
nr_scell_info_v3_t61
IBIOgrsRelayLikelihood
sw1_sw2_t5
IBI_NET_NW_CONN_TYPE_LEGACY
IBICpsCellularPowerReportState
loopback_id_t3
IBI_NET_VOIMS_CALL_RAT_SWITCH_FAILURE
lte_ncell_info_t15
(%s:%d) Client(0x%04x: %s) enter-LPM done
(%s:%d) Client %s has NO indications registered
message_sequence_number_t5
IBI_CALL_CS_ERROR_CAUSE_CDMA_TC_RELEASE_ACK_FAIL
IBI_CALL_CS_TEMP_FORBIDDEN_CALL_ATTEMPT
eCSI_ICE_TS_ANTENNA_STATE
IBI_CALL_CS_MS_CONN_REJECT_REDIRECTION
IBI_CALL_CS_RADIO_LINK_FAILURE_DETECTED
sessionId_t13
UtaIdcRTSetScanFreqReq
laa_threshod_out_t5
type_t4
IBI_SS_LCS_POS_CAP_GNSS_AD_GLONASS
hrpd_nai_data_t8
(%s:%d) Sending for cid 0x%x (cur %zu max %u) %s
service_type_t3
emergency_bearer_supported_t5
peripheral_t1
cert_identifier_len_t7
IBICallPsDataTransferTimeRspCb
vLqm_blob_t5
network_ims_voice_over_ps_supported_t35
ssrc_t4
get_input_V1_t26
OdttRunRspCb
file_name_t2
registration_mode_t3
IBIOgrsDedicatedDiscoveryReq
IBI_CALL_CS_FAX_CALL
IBI_SMS_NO_CARRIER_DUAL_SIM_CONFLICT
/Library/Caches/com.apple.xbs/E497E93F-14A7-4885-82BD-D54E476F8AAB/TemporaryDirectory.ZrAZ7x/Sources/AppleRemoteInvocation/common/inc/ari_sdk_msg.h
SIM_MAP_SUCCESS
IBIUInt64
(%s:%d) Dropping optional TLV(%s) for MSG(%s) with packed sz(%zu) not multiple of element encoded size(%zu)
IBISimTkDtmfString
earfcn_t6
local_ip_t6
IBI_LP_GANSS_ID_GLONASS
IBI_NET_NW_CONN_TYPE_5G
(%s:%d) Couldn't unpack response for setting wakeable attribute
IBI_NET_BAND_LTE_17
IBIMsLpPosIs801GpsLocationIndCb
{0x%04x, 0x%04x},\n
IBIRfPortMapStatus
full_access_granted_t3
reject_cause_t4
IBI_OGRS_MASTER_LIKELIHOOD_Always
search_string_t11
procedure_result_t3
is_oriented_to_target_t2
ARI_BBFW_RESET_E
IBI_NET_REGISTRATION_REJECT_CAUSE_DUAL_SIM_CONFLICT
IBICallPsPagingWithPermIdInfo
IBI_OGRS_DEACTIVATION_CAUSE_Max
num_pf_v2_t28
IBINetUserPlaneCIoTOptimizationSupport
cause_t16
returnCode_t2
config_type_t2
ap_rat_switch_result_t2
IBI_CALL_PS_RESULT_CODE_MAX_DATA_RATE_USER_PLANE_INTEGRITY_PROTECTION_TOO_LOW
IBI_LP_IS801_LOCATION_IND_ERROR
IBIImsMEMediaCapability
~Semaphore
IBI_NET_ERROR_LADN_NOT_AVAILABLE
IBI_NET_FD_DISCARD_CAUSE_DEFAULT
IBI_NET_FD_DISCARD_CAUSE_TE_BACKG_CALL
IBI_SIM_USIM_ENH_SEARCH_FROM_OFFSET_FORWARD_FROM_SPECIFIED_REC
dns_protocol_type_t33
IBISimTkCallControlResult
actual_file_size_bytes_t7
IBI_CALL_CS_ERROR_CAUSE_CDMA_ORIG_USER_CANCEL
IBI_NET_BAND_NR_22
skey_hash_t1
IBI_CALL_CS_MS_MSG_TYPE_NON_EXISTENT
IBI_CALL_PS_RESULT_CODE_GPRS_SERVICES_AND_NON_GPRS_SERVICES_NOT_ALLOWED
IBI_LP_GANSS_ID_INVALID
IBI_OGRS_SYSTEM_STATUS_Max
result_t6
configuredSimInfo_t2
AriGmid
IBI_CDMA_ERROR_CLASS_PERMANENT
trigger_time_ms_t5
rat_mode_settings_V2_t12
IBI_IMS_ME_MEDIA_TYPE_RTT
is_pso_supported_t4
IBI_NET_BAND_NR_4
IBI_VINYL_TAPE_CMD_CANCEL_SESSION
language_notification_t17
CsiIceGetAntennaStateRspCb
apacs_type_t4
0x%04x
IBI_SIM_ALWAYS
sim_indicator_t7
is_always_on_t30
accessory_state_t1
IBI_CALL_CS_CHANNEL_UNACCEPTABLE
IBI_CALL_CS_CALL_MODIFY_REJECTED
IBI_CALL_PS_PIPE_TYPE_UL_TR
IBIMsLpDiscardedPosSessionIndCb
cdma_evdo_scell_info_t35
boot_id_t2
IBI_SS_LCS_POS_CAP_NR_ECID_SUPPORT
rsp_param_v2_t3
IBI_NET_NR_CELL_GROUP_PRIMARY
num_trans_id_t19
t_s_UtaIdcMiscConfigV2
IBI_NET_REGISTRATION_REJECT_CAUSE_ATTACH_NOT_ALLOWED
IBI_NET_NW_UP_CIOT_OPTIMIZATION_NOT_SUPPORTED
apn_t4
nr_ncell_info_t48
UserList_t4
IBI_NET_BAND_UMTS_TDD_D
IBI_NET_USER_CAUSE_POWER_DOWN
gsm_ncell_info_t13
cdma_bands_t11
IBISimPbLocationIndCb_V1
ecc_category_t12
ARI_ATTR_OFF
IBI_NC_RESULT_SIM_NOT_READY
error_cause_t4
existing_manifest_t2
gsm_scell_info_t7
IBI_SIM_APDU_CMD_EOF_REACHED
ganssLocationInfo_t7
IBINetSignalQuality
handler == NULL
IBISimSecImpi
IBI_CALL_CS_CALL_IS_CLEARED
IBI_CALL_PS_VOIP_CALL_ACTIVE
cacheStatus_t2
IBI_NET_RAT_5G_SIB2_PLMN_R15
IBI_NET_PLMN_NAME_SOURCE_NOT_FOUND
IBICallPsRtpRspCb
IBI_CALL_PS_RESULT_CODE_CONTROL_BY_SIM_BUSY
IBI_SS_NET_ERROR_MAX_NUMBER_OF_MPTY_PARTICIPANTS_EXCEEDED
IBI_VINYL_ATC_SUCCESS
velocityEstimate_t9
altUncert_t11
cid_t2
IBINetRatModeSettingExt
IBI_CALL_CS_MS_L2_CAUSE_T200_EXP_N200_PLUS_1_TIMES
IBI_CALL_PS_DELIVERY_ORDER_YES
IBI_CALL_PS_RESULT_CODE_INVALID_TRANSACTION_IDENTIFIER_VALUE
IBI_CDMA_PS_RAT_EHRPD
IBICallPsReservePDUSessionIDReq
cdma1x_scell_info_t22
ecc_category_t10
IBIApacsDataStatusRspCb
IBI_NET_PSSI_NR_SCS_240KHZ
IBI_VINYL_PRLACT_SIM_MAX_NUM_APP
num_of_idle_conns_t4
lte_ncell_info_valid_t23
IBICSGIndicatorT
IBINetApCarplayInfo
IBIOgrsPresenceDiscoveryStopRspCb
SearchList_t6
IBICallPsPacketFilter
SendInternal_block_invoke
IBIStwSetConcurrencyConfigReq
IBI_NET_BAND_LTE_INVALID
IBI_NET_DC_VOICE_DOMAIN_PREFERENCE_CS_ONLY
IBIMsLpMeasurePositionReqCb
location_privacy_mode_t9
ltl_cleanup_factor_t9
IBIMSimGetSimStackMappingRspCb
IBI_CALL_CS_MS_ABNORMAL_RELEASE_TIMER_EXPIRED
IBI_CALL_CS_RETRY_CAUSE_IMS_SERVICE_NOT_AVAILABLE
ICE_CPR_STATE_VOICE_CALL
IBI_SIM_PB_RESULT_ERROR_REFERENCE_ERROR
IBICallPsWrmSdmLocationDBInfoRsp
t_s_UtaIdcUwbRtActivityMitigationPolicyConfigV2
IBI_CALL_CS_SUCCESS
IBI_SIM_PB_VALID_FLAG_NONE
ps_state_t1
INVALID AriMsg buffer.
IBI_CALL_CS_UNEXPECTED_ERROR
IBI_NET_DC_IMS_SESSION_STARTED
IBI_NET_ERROR_RETRY_ON_NEW_CELL_BEG
VINYL_RESULT_INVALID_SLOT
plmn_id_t4
IBI_CALL_PS_SUSPEND_CAUSE_RAT_CHANGE
IBI_NET_DORMANCY_STATUS_ACTIVE
IBI_SS_NET_REJECT_BADLY_STRUCTURED_COMPONENT
IBI_VINYL_TAPE_CMD_GET_EUICC_CONFIGURED_ADDRESS
IBI_CALL_CS_VOIMS_RTP_SESSION_DIR_DL_AND_UL
IBI_NET_AP_CARPLAY_TYPE_WIRED
IBI_SS_LCS_POS_CAP_GNSS_SYSTEM_GSM_GPS_SUPPORT
IBI_SS_NET_ERROR_ILLEGAL_EQUIPMENT
IBIMsLpWlanMeasurementRspAckCb
IBINetGetCellInfoReq
CsiFpUpdateHeader
IBISimPbWriteEntryReq
IBI_HEALTH_ACTIVITY_TYPE_ELLIPTICAL
IBI_NET_BAND_LTE_25
IBI_SMS_TP_INVALID_SC_ADDRESS
security_context_t3
IBI_CALL_PS_MEAN_THROUGHPUT_10K
APACS_STATUS_LOCATION_SERVICES_AVAILABLE_NOW
IBI_EOS_STATE_UNKNOWN
IBI_NET_NEIGBOURING_CELL
IBI_NET_NR_CELL_GROUP_MAX_COUNT
IBI_OTASP_STATUS_OTAPA_STOPPED
IBI_VIYNL_PRLACT_SIM_SECURITY_CONTEXT_USIM_3G
no_of_sms_entries_t2
IBISimPinStatus
IBI_NET_BAND_NR_77
IBICallPsTransmitStateReq
(%s:%d) Request to set %s as NON-wakeable.  Ignoring...
IBI_OGRS_PDP_DEACTIVATION_CAUSE_NotDiscovered
IBI_SIM_FCP_SEC_ATTR_REF_TYPE_REC
IBI_SS_SV_CODE_CLIP
response_t1
IBI_NET_NR_FREQ_TYPE_NONE
IBIImsMERtcpSenderReportIndCb
send_sms_V1_t27
t_s_UtaIdcCameraStatusV2
IBINetNssaiInfoRspParam
InterfaceID_t2
IQCAP_ACTIVITY_FAILED_INCORRECT_STATE
IBI_PRI_STATUS_SIGN_REJ_BY_SECURITY
IBICallPsWrmSAInfoReq
IBINetEnabledRats_V2
IBI_NET_REGISTRATION_MODE_MANUAL
IBI_NET_TIMER_DEACTIVATED
IBIMsSsLcsMtlrNotificationIndCb
IBI_CALL_CS_IS_ECT
IBI_CDMA_SMS_ERR_CAUSE_NW_RESOURCE_SHORTAGE
IBIEmergencySessionState
IBI_CALL_CS_ERROR_CAUSE_CDMA_REORDER
IBIPsTCPUDPFilterType
plmn_w_ac_t_t4
SIM_CARD_5
17_ims_me
IBIImsMEMediaSessionErrIndCb
dtmf_code_t4
plmn_t2
(%s:%d) cid 0x%x not registered
IBINetNitzInfoIndCb_V1
IBI_IMS_ME_AUDIO_BAND_NB
IBI_SIM_APDU_CMD_OTHER
IBI_SIM_TK_COMMAND_TYPE_SEND_PROVIDE_LOCAL_INFO
slot2_is_embedded_t30
evs_codecs_length_t24
(%s:%d) Destroy transaction manager for cid 0x%x
IBI_CDMA_LANGUAGE_ICELANDIC
CsiIceGetTxAntennaReq
change_data_t6
IBIVinylPrlActProfilePINStatus
IBI_SS_LCS_POS_CAP_LTE_SON_ACTIVE_POS_FLAG
(%s:%d) Attempt to release ctx 0x%04x.  Ignoring...
distortion_time_t2
UtaIdcSetCnvAntBlockPwrLmtConfigReqV2
IBIStwV2ServiceType
main_fw_size_t14
IBI_SIM_TK_CALL_CONTROL_RESULT_ALLOWED_MODIFIED
IBI_SS_MM_MSG_TYPE_NOT_COMPATIBLE_WITH_PROTOCOL_STACK
IBIPsIPMaskFilterType
IBIVinylM4OemData
ICE_IBI_APACS_PUSH
IBIPriFileStatus
CsiSahClearCrashResportRspCb
CsiIceAudSetAudioLoggingRespCb
vocoder_samplerate_t6
ecc_length_t2
wrist_state_t1
IBI_CLS_POS_CAP_MDT_SON_LOCATION_SUPPORT
IBI_SIM_VERIFIED
IBI_SS_GSM_ERROR_REQUESTED_CIRCUIT_NOT_AVAILABLE
IBISimApplicationActivity
data_t3
control_t1
ims_emergency_supported_t21
msg_id_t1
IBI_OGRS_PDP_DEACTIVATION_CAUSE_Max
IBI_SS_MM_MAC_FAILURE
is_data_stall_enabled_t12
IBI_LP_UDRE_SCALE_0_75
IBI_SS_MM_IMSI_UNKNOWN_IN_VLR
tp_presence_t6
(%s:%d) CopyEncodedMessage fails on msg(%p)
IBISimTkProactiveCmdSendSms_V1
IBISsServiceCode
clir_cause_t9
UtaIdcSetCriticalCarrierConfigRspCbV2
IBIVinylPrlActAuthParam
UtaIdcGetCellConfigRspCb
IBINetRRCReleaseChangeInfoInd
sim_pin_t6
IBI_CALL_CS_REJ_BY_CALL_CONTROL
IBI_CALL_CS_CALL_IS_HELD
IBI_SIM_PB_RESULT_ERROR_USIM_PB_NOT_READY
IBI_SS_NET_REJECT_MISTYPED_COMPONENT
IBICallPsDataStallEnable
lte_scell_info_r15_t44
IBINetGsmcellInfoList
CsiIdcTestModeCmdRsp
IBINetPowerDownReq
warning_area_coord_length_t11
IBI_CALL_CS_CMD_SET
beta3_t9
UtaIdcSetUwbAntBlockPwrLmtConfigRspCb
IBINetGetPlmnNameInfoRspCb_V1
ARI_VALIDATE_WRONG_MSGID_E
IBI_SIM_TK_ENVELOPE_TYPE_EVENT_DOWNLOAD_USER_ACTIVITY
received_mw_t1
t_s_UtaIdcMiscConfigV3
eps_qos_t11
rec_num_t3
pkt_seq_t2
IBI_SMS_TP_FCS_NO_SC_SUBSCRIPTION
sessionInfo_t3
IBICallPsCriticalPsSessionReq
CsiIpcCtrlPathTestInitReq
IBIXccClockControlIndCbParams
IBI_EVS_32_0_Kbps
IBI_CALL_PS_MODULATION_SCHEME_QPSK
IBI_CALL_PS_RESULT_CODE_MESSAGE_NOT_COMPATIBLE_WITH_PROTOCOL_STATE
IBICallPsStopBandwidthEstimationRspCb
udp_src_port_t6
encryptionStatusInfo_t3
(%s:%d) Create transaction manager for cid 0x%x
IBI_CALL_PS_SM_CAUSE_ACCEPT_SINGLE_ADDR_BEARERS_ONLY_ALLOWED
bDSMIPv6_haar_t14
rtt_t12
IBIFilerHSReadBBReq
~TransactionMgr
UtaIdcSetCnvAntBlockPwrLmtConfigReq
IBISimPbLocationInfo
IBI_NET_ERROR_PLMN_NOT_ALLOWED_AT_PRESENT_LOCATION
IBICallPsLoopbackPipeConfig
msg_t4
IBICallCsVoimsSrvccHoStatus
IBI_CALL_CS_TEMP_FORBIDDEN_CALL_ATTEMPT_LIMITED_SERVE
IBI_IMS_ME_RTT_SESSION_TTY_OFF
IBI_NET_UMTS_PWR_CLASS_4
IBI_SIM_CMD_INCORRECT_PARAM_IN_DATA_FIELD
IBI_SMS_MSG_NOT_COMPATIBLE
IBI_SS_MSC_NOT_REACHABLE
IBI_MSIM_REMAP_NEEDED
IBI_MSIM_SET_DATA_SIM_CAUSE_NO_SERVICE
simtk_transaction_id_t2
UtaIdcSetRTFeatureSpmiTxRspCbV3
mid_range_list_t3
IBI_SIM_CHV1_REQUIRED
IBI_SIM_SUCCESSFUL
is_enciphered_t3
CsiBspSwTrapReq
vocoder_type_t5
UtaIdcSetCamAntBlockPwrLmtConfigReq
UtaIdcRTSetScanFreqRspCbV2
sessionProtocol_t7
qos3g_v1_t15
IBISimTkImsCcData
send_mode_t5
t_s_UtaIdcTxBlankingConfig
conn_type_t5
IBI_CALL_PS_RESULT_CODE_MULTIPLE_PDN_CONNECTIONS_FOR_A_GIVEN_APN_NOT_ALLOWED
IBI_SIP_EVENT_OUTGOING_SESSION_EST
IBICallCsAudioControl
IBI_SIM_TK_PROACTIVE_CAUSE_USER_DID_NOT_ACCEPT_CALL_SETUP_REQUEST
, ... skipping after (%d) to last a few ... 
nr_ncell_info_t56
wci2_msg6_t8
coding_scheme_t2
IBI_SIM_RFU_TYPE
IBI_SMS_TP_FCS_UNSPEC_TP_CMD_ERROR
IBI_RAT_NR
IBI_VINYL_TAPE_CMD_AUTHENTICATE_SERVER
IBI_FILER_HS_COMPRESSION_LZBITMAP
IBI_MESSAGE_MODE_3GPP2
IBI_STW_STATE_DEACTIVATE
cf_list_length_t6
IBICallCsFeat
IBIOgrsEmergencyReceptionIndCb
IBI_CALL_CS_OPERATOR_BARRING
IBI_CALL_CS_USER_BUSY
IBI_NET_REGISTRATION_STATUS_PS_EMERGENCY
IBI_CALL_PS_RESULT_CODE_PCO_SET_FAILURE
IBI_NET_BAND_NR_67
IBI_SIM_IND_NOT_PRESENT
IBIAccFreqReportingType
IBICbsType
IBI_SIM_CMD_FILE_NOT_FOUND
IBI_SIM_CMD_TECHNICAL_PROBLEM
IBI_SS_SV_CODE_CF_ALL
IBI_NET_CELL_NWID_GNB_SW_25R3_NOKIA
path_t6
IBIImsMEMediaType
cid > ARI_MAX_CLIENT_ID
IBI_NET_AP_CARPLAY_TYPE_WIRELESS
IBI_NET_FD_DISCARD_CAUSE_SIG_CS
IBI_SMS_HANDOVER_IMPOSSIBLE
tempIDUpdateStatusInfo_t6
pkt_offset_t4
IBI_SIM_NOT_NEEDED
IBI_SIM_TK_SETUP_CALL_RESERVED
arrival_time_t5
SrcCfgParam_t1
location_info_t9
IBICallCsCrssRspCb
IBICsgInfo
IBI_NET_SIGNAL_QUALITY_GSM
verticalConfidence_t11
IBIMSimConfigParam
IBI_CALL_CS_DUAL_BS61
IBI_SMS_MS_NORMAL_EVENT
IBIMsLpGlonassNavigationModelIndCb
cdma_1x_eri_t27
AriCheckin
IBICallCsStopDtmfExtRspCb
IBI_SS_GSM_ERROR_ACM_GREATER_OR_EQUAL_TO_ACM_MAX
wnt_t5
IBINetTimerInfoIndCb
subscription_type_t3
IBI_NET_BAND_GSM850
(%s:%d) Setting indication %s to wake AP failed via ctx 0x%x (Received NACK, reason unknown due to malformed NACK)
language_cnt_t8
serial_number_t3
IBI_OTASP_STATUS_IMSI_DOWNLOADED
IBI_SIM_CMD_MORE_DATA_EXPECTED_PROACTIVE_CMD_PENDING
IBI_SIM_RES_TYPE_WRONG_CID
IBI_SIM_PB_RESULT_ERROR_WRONG_INSTRUCTION_CLASS
num_pf_v2_t41
12_sim_sec
distortion_duration_t3
is_emergency_normal_t17
IBI_CALL_PS_RESULT_CODE_NETWORK_FAILURE
IBI_SIM_TK_COMMAND_TYPE_GET_INPUT
IBICallPsGetBandwidthEstimationInfoRspCb
IBINetUserCause
warning_t9
IBI_CDMA_SMS_ERR_CAUSE_GENERAL_OTHER
IBI_NC_RESULT_INVALID_PARAM
pco_params_t22
IBI_CALL_CS_MTC_CALL_CONFIRMED
IBI_CALL_PS_RESULT_CODE_NO_RESPONSE_TIMEOUT
IBISimFileReadBinRspData
gpsWeekCycleNumber_t10
UtaIdcSetRTFeatureSpmiRxReqV2
IBI_CALL_PS_WIFI_CALL_SIM_SLOT_1
IBI_IMS_ME_DTMF_DIGIT_CODE_4
IBI_SMS_MS_CELL_BARRED
IBICallPsDataCallStoppedIndCb
(%s:%d) Transaction no longer exist for ctx 0x%04x; ignoring cancel for %s
p_data_t4
IBINetImsVoPSSupport
IBI_CALL_CS_VOIMS_MMTEL_SESSION_HOLD_ASSIST_FINISHED
IBI_SMS_ERROR_CAUSE_NONE
active_sleep_t2
CsiIdcUartType4StatsRspCb
/Library/Caches/com.apple.xbs/E497E93F-14A7-4885-82BD-D54E476F8AAB/TemporaryDirectory.ZrAZ7x/Sources/AppleRemoteInvocation/common/inc/ari_utils.h
grip_state_t1
IBI_SIM_PIN_NO_KEY
IBI_VINYL_ATC_WRONG_PROFILE_RE_ENABLING
tag_type_t6
(%s:%d) Invoked with illegal buffer(%p) or size(%u)
connected_no_t3
UtaIdcSetWiFiAntBlockPwrLmtConfigReq
IBI_CALL_PS_IP_TYPE_V4_V6
IBISmsGetServiceStatusRspCb
ARI_ATTR_SET
AriUtaModeInitialSwitchCompleteIndCb
IBI_CALL_PS_DELIVERY_ORDER_NO
IBI_CALL_PS_RESULT_CODE_CSG_UNAUTHORIZED
IBI_NR_FREQ_RANGE_FR1
IBI_SIM_ACCESS_APP_TYPE_UNKNOWN
CsiTraceProfilePacketsReq
UtaIdcSetTunerArbitrationConfigReqV2
IBI_SIM_TK_COMMAND_TYPE_DISPLAY_TEXT
IBI_VINYL_TAPE_CMD_GET_EUICC_INFO
IBI_CALL_PS_RESULT_CODE_MS_INTERNAL_FAILURE
setup_idle_mode_text_t16
IBIStwV2GpsDataUpdateRspCb
IBI_CALL_CS_FACILITY_NOT_IMPLEMENTED
record_number_t5
(%s:%d) Fatal to send requests against transaction manager of cid 0x%x
IBI_LP_MULTI_PATH_LOW
IBI_OGRS_MASTER_LIKELIHOOD_Level1
qos_3g_present_t34
p_data_t3
IBI_VINYL_PRLACT_PROFILE_PIN_DISABLED
(%s:%d) Message(%s)'s mandatory TLV (%d) not packed!
CsiIceAudVocoderInfoRespCb
IBI_CPS_NSSAI_MAPPED_HPLMN_SST_PRESENT
IBI_LP_GPS_DOPPLER_UNCER_EXT_D60
IBI_NET_BAND_NR_261
IBI_CALL_PS_PROTO_MAXENUMSIZE
alfa0_t3
IBI_CALL_PS_RESULT_CODE_DETERMINED_BARRING
IBI_NET_ERROR_TEMPORARILY_NOT_AUTHORIZED_FOR_THIS_SNPN
IBI_NET_FD_DISCARD_CAUSE_DTM_NOT_SUPPORT
IBI_SS_LCS_POS_CAP_LPP_WLAN_MEAS_SUPPORTED
scrt_blob_data_t2
IBI_CALL_PS_DNS_PROT_DTLS
IBI_CDMA_SMS_ERR_CAUSE_MISSING_MAND_PARAM
IBI_NET_CELL_NWID_GNB_SW_UNKNOWN
IBIMsLpGpsAlmanacIndCb
hemisphere_t3
cdma_ps_rat_t130
IBICallPsSessionId
IBI_CALL_PS_AV_STREAMING_ON
IBI_CLS_POS_CAP_LPP_WLAN_MEAS_SUPPORTED
AP_5G_RAT_SWITCH
```
