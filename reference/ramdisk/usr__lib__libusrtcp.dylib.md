# `/usr/lib/libusrtcp.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 655,712 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2224)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/usr/lib/libusrtcp.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/System/Library/Frameworks/Network.framework/Network (compatibility version 1.0.0, current version 6681.52.6)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,125)

```
%{public}s %{public}s tcp_unlock: so=%p usecount=%x lrh= %s, backtrace limit exceeded
%{public}s Assert so != NULL failed
%{public}s source_offset < 0
%{public}s source_offset < 0, no backtrace
%{public}s called with null tcp, no backtrace
%{public}s %{public}s write timeout
%{public}s %{public}s tcp_set_fast_open_force_enable failed %{darwin.errno}d, no backtrace
%{public}s called with null link_info
%{public}s register notification for %{public}s called with zero length
%{public}s %{public}s so=%p head still exist
%{public}s %{public}s apply socket parameters failed, backtrace limit exceeded
%{public}s %{public}s got connect event
%{public}s %{public}s tcp_set_write_timeout failed %{darwin.errno}d
%{public}s %{public}s tcp_getlock: so=%p usecount=%x lrh= %{public}s
%{public}s bytes_sacked (%u) can't be smaller than already SACKed segment length (%u)
%{public}s bytes_sacked (%u) can't be smaller than already SACKed segment length (%u), backtrace limit exceeded
%{public}s %{public}s improperly called sodefunct, backtrace limit exceeded
%{public}s %{public}s tcp_set_enable_l4s failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_NOOPT failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s called with null (dscp_value <= _MAX_DSCP), dumping backtrace:%{public}s
%{public}s called with null protocol, no backtrace
%{public}s nw_protocol_tcp_obj_alloc failed, dumping backtrace:%{public}s
%{public}s %{public}s tcp_set_traffic_class failed %{darwin.errno}d, no backtrace
%{public}s %{public}s tcp_set_keepalive_idle_time failed %{darwin.errno}d
%{public}s %{public}s is already connected
%{public}s %{public}s tcp_set_keepalive_interval failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s bytes_lost (%u) can't be smaller than already lost segment length (%u), dumping backtrace:%{public}s
%{public}s new CE count (%llu) can't be less than current CE count (%llu)OR newly ACKed (%llu) can't be less that current ACKed (%llu)
%{public}s %{public}s tcp_setsockopt TCP_CONNECTIONTIMEOUT failed %{darwin.errno}d, no backtrace
%{public}s %{public}s setup state failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s tcp_bind failed, dumping backtrace:%{public}s
%{public}s called with null object, dumping backtrace:%{public}s
%{public}s %{public}s inp %p invalid wantcnt %d, so %p [%d] usecount %d retaincnt state 0x%x flags 0x%x, no backtrace
%{public}s %{public}s pcb=%p so=%p usecount is negative, dumping backtrace:%{public}s
%{public}s ICMP response for ineligible TCP seq num (%d, una %d max %d)
%{public}s %{public}s tcp_getlock: so=%p usecount=%x lrh= %{public}s, no backtrace
%{public}s called with null frame, no backtrace
%{public}s %{public}s tcp_set_no_delay failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s tcp_disable_blackhole_detection(so) %{darwin.errno}d
%{public}s %{public}s tcp_setsockopt TCP_KEEPCNT failed %{darwin.errno}d, no backtrace
%{public}s tcp->release_is_delayed already set
%{public}s Segment ACKed list shouldn't contain any segments as they are removed immediately after being ACKed
%{public}s %{public}s assertion failure SEQ_GEQ(tcp_hdr->th_ack, tp->snd_una) %u:%u tlen %u, flags=%{network:tcp_flags}x seq=%u, ack=%u, win=%u state=%{network:tcp_state}x rcv_nxt=%u, snd_una=%u, no backtrace
%{public}s Attempt to set generation-count on a chain-member, backtrace limit exceeded
%{public}s %{public}s pcb=%p so=%p usecount is negative
%{public}s %{public}s pcb=%p so=%p usecount is negative, backtrace limit exceeded
%{public}s %{public}s pcb=%p release with zero count, dumping backtrace:%{public}s
%{public}s Copied %zu out of expected %u bytes, no backtrace
%{public}s called with null handle
%{public}s Aggregate buffer length: %u sum: %u
%{public}s %{public}s ECN flags (0x%x) not set correctly, backtrace limit exceeded
%{public}s Attempt to set generation-count on a chain-member, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_NOTIMEWAIT failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s force closing tcp
%{public}s %{public}s rt_heur rt_heur_alloc unexpectly set
%{public}s %{public}s dropping a completely overlapping segment: tqe_seq %u th_seq %u tqe_len %u tlen %u
%{public}s %{public}s not enough space to add any AccECN option
%{public}s %{public}s tcp_unlock: so=%p usecount=%x lrh= %s
%{public}s %{public}s found data to carry wake packet
%{public}s tcp->release_is_delayed set during dispose, dumping backtrace:%{public}s
%{public}s %{public}s tcp signal error: %d
%{public}s %{public}s processing an input-frame, %u:%u tlen %u, flags=%{network:tcp_flags}x seq=%u, ack=%u, win=%u state=%{network:tcp_state}x rcv_nxt=%u, snd_una=%u
%{public}s %{public}s new_frame has next
%{public}s %{public}s no other reference on socket, no backtrace
%{public}s %{public}s retiring defunct socket from the TCP timer list (wantcnt=%d)
%{public}s %{public}s pcb=%p release with zero count, backtrace limit exceeded
%{public}s called with null invalid len %d, dumping backtrace:%{public}s
%{public}s requested frame count %u larger than max frame count %u
%{public}s Bad link elm %p next->prev != elm, backtrace limit exceeded
%{public}s Existing metadata %p doesn't match expected %p, backtrace limit exceeded
%{public}s 
%{public}s called with null (len == sizeof(bool)), backtrace limit exceeded
%{public}s frame_array %p not empty, dumping backtrace:%{public}s
%{public}s %{public}s tcp get heuristics failed, no backtrace
%{public}s Underflow: %{public}s, decrement %llu, result %llu, backtrace limit exceeded
%{public}s tcp_trigger_connect failed %{darwin.errno}d
%{public}s %{public}s tcp_set_keepalive_interval failed %{darwin.errno}d, backtrace limit exceeded
%{public}s Assert SACK_ENABLED(tp) failed
%{public}s failed to release inpcb reference
%{public}s called with null (max_frame_count > 0), dumping backtrace:%{public}s
%{public}s called with null (max_frame_count > 0), backtrace limit exceeded
%{public}s Invalid frame metadata %p
%{public}s called with null (buffer_size > 0), dumping backtrace:%{public}s
%{public}s %{public}s got mtu %d, ifindex %d, offloads %#x
%{public}s %{public}s tcp_setsockopt TCP_KEEPCNT failed %{darwin.errno}d
%{public}s Bad link elm %p prev->next != elm
%{public}s %{public}s tcp_set_notsent_lowat failed %{darwin.errno}d, no backtrace
%{public}s %{public}s tcp_set_keepalive_idle_time failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s Assert nsack == 0 || tp->rcv_numsacks >= nsack failed
%{public}s %{public}s tcp_unlock: so=%p NO PCB usecount=%x lrh= %s, no backtrace
%{public}s called with null (buffer_size > 0), backtrace limit exceeded
%{public}s %{public}s tcp_set_max_pacing_rate failed %{darwin.errno}d, backtrace limit exceeded
%{public}s Attempt to get generation-count on a chain-member, no backtrace
%{public}s %{public}s dropping connection on keepalive timeout
%{public}s called with null tfo_cache_buffer, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_NOTIMEWAIT failed %{darwin.errno}d
%{public}s tcp_get_southbound_frame failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s tcp_set_write_timeout failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s invalid frame list
%{public}s %{public}s chained frame len %u is smaller than TCP header size %u, no backtrace
%{public}s failed to allocate slab buffer of size %u
%{public}s called with null frame->finalizer, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_KEEPCNT failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s Old input handler does not match (%p != %p), backtrace limit exceeded
%{public}s %{public}s failed to finalize checksum, %s
%{public}s bytes_lost (%u) can't be smaller than already lost segment length (%u), backtrace limit exceeded
%{public}s Assert globals->tcbinfo != NULL failed
%{public}s %{public}s %{public}s t_state %{public}s tcp_packet_chaining %d
%{public}s INADDR_BROADCAST destination not supported
%{public}s nw_endpoint_get_address failed, backtrace limit exceeded
%{public}s %{public}s past connected state, skipping
%{public}s %{public}s capping minimum_bytes %u to sb_hiwat %u
%{public}s bytes_retransmitted (%u) can't be smaller than retransmited segment length (%u), no backtrace
%{public}s %{public}s NBIO not set, dumping backtrace:%{public}s
%{public}s %{public}s %{public}s t_pktlist_sentlen %d t_lastchain %d
%{public}s %{public}s %{public}s: sb %p so %p cc %d mb %p
%{public}s %{public}s so %p [%d] usecount %d, no backtrace
%{public}s %{public}s so=%p head still exist, backtrace limit exceeded
%{public}s %{public}s tcp_set_fast_open_force_enable failed %{darwin.errno}d, backtrace limit exceeded
%{public}s ipi %p already in the list
%{public}s Assert globals->free_slab_frame_count > 0 failed
%{public}s called with null (len == sizeof(struct nw_link_congestion_info))
%{public}s %{public}s t_pktlist is not empty in tcp_close, dumping backtrace:%{public}s
%{public}s Assert tp->sackhint.sack_bytes_acked >= 0 failed
%{public}s g_tcp_nw_assert_context is %s value %lld
%{public}s Assert tp->t_ccstate->cub_origin_point > 0 failed
%{public}s %{public}s RELEASE pcb=%p so=%p usecount is negative, backtrace limit exceeded
%{public}s %{public}s keepalive
%{public}s setsockopt TCP_ECN_MODE failed %{darwin.errno}d
%{public}s Old input handler does not match (%p != %p), no backtrace
%{public}s %{public}s dropping frame of length %u
%{public}s %{public}s segmentation_offload_notification disabled
%{public}s %{public}s os_nexus_flow_set_connection_idle returned %d
%{public}s called with null handle, no backtrace
%{public}s failed to acquire inpcb reference
%{public}s nw_endpoint_get_address failed, no backtrace
%{public}s %{public}s tcp_setsockopt TCP_CONNECTIONTIMEOUT failed %{darwin.errno}d
%{public}s Old input handler does not match (%p != %p), dumping backtrace:%{public}s
%{public}s %{public}s inp_fc_unthrottle_tcp keep rxmit state t_rxtshift %d
%{public}s %{public}s sb=%p sb_flags=0x%x sb_so=%p usecount=%d, no backtrace
%{public}s invalid packet service class %d
%{public}s called with null frame
%{public}s called with null frame->finalizer, backtrace limit exceeded
%{public}s nw_endpoint_get_address failed, dumping backtrace:%{public}s
%{public}s %{public}s tcp disconnected
%{public}s %{public}s remove_input_handler is not valid
%{public}s %{public}s link heuristics %s
%{public}s %{public}s tcp_getlock: so=%p NULL so_pcb %{public}s, no backtrace
%{public}s TCP route unusable, backtrace limit exceeded
%{public}s Underflow: %{public}s, decrement %llu, result %llu, no backtrace
%{public}s called with null (dscp_value <= _MAX_DSCP), no backtrace
%{public}s %{public}s nw_endpoint_get_address failed, dumping backtrace:%{public}s
%{public}s called with null (len == sizeof(bool)), no backtrace
%{public}s %{public}s ourfinisacked t_state %{public}s
%{public}s %{public}s level %{public}s flow %{public}s defunct
%{public}s %{public}s throttling is now %s
%{public}s %{public}s so_usecount %u added to TIME_WAIT delay %u
%{public}s %{public}s tcp_set_fast_open_force_enable failed %{darwin.errno}d
%{public}s %{public}s tcp_set_keepalive_idle_time failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s sending frame, %u:%u tlen %u, flags %#x, seq %u, ack %u, rcv_nxt %u snd_una %u state %u svc %{public}s
%{public}s %{public}s SB_DROP not set, backtrace limit exceeded
%{public}s %{public}s soclose: NOFDREF, no backtrace
%{public}s called with null globals, no backtrace
%{public}s Assert tp->sackhint.sack_bytes_rexmit >= 0 failed
%{public}s Failed to extract data from frame, no backtrace
%{public}s called with null ret_frame_array
%{public}s nw_queue_context_create_source failed, backtrace limit exceeded
%{public}s %{public}s nam is NULL, no backtrace
%{public}s %{public}s tcp_get_northbound_frame, returned NULL %{darwin.errno}d, no backtrace
%{public}s Failed to copy expected bytes, total_space %u != adj_space %u
%{public}s called with null (buffer_size > 0)
%{public}s uTCP external frame not marked
%{public}s %{public}s Segment count is 0 for single-IP frame, backtrace limit exceeded
%{public}s %{public}s path is non-viable, dropping output
%{public}s Assert num_sack_blks <= (TCP_MAX_SACK + 1) failed
%{public}s %{public}s tcp_set_traffic_class failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s nw_endpoint_get_address failed
%{public}s PCB marked as WNT_STOPUSING, exiting early
%{public}s %{public}s recv_bg: cleared (was %{public}s)
%{public}s called with null (max_frame_count > 0)
%{public}s Frame does not use external data
%{public}s called with null tcp, dumping backtrace:%{public}s
%{public}s %{public}s apply socket parameters failed, no backtrace
%{public}s %{public}s nam is NULL, dumping backtrace:%{public}s
%{public}s called with null new_input_handler, backtrace limit exceeded
%{public}s %{public}s tcp_get_northbound_frame, returned NULL %{darwin.errno}d, backtrace limit exceeded
%{public}s called with null link_info, no backtrace
%{public}s %{public}s setup state failed %{darwin.errno}d, no backtrace
%{public}s %{public}s output protocol is disconnected
%{public}s %{public}s called with error: %d
%{public}s %{public}s nw_protocol_tcp_set_connection_idle flow_registration is NULL
%{public}s RB tree still contains segments while time ordered list is already empty
%{public}s Assert len <= TFO_COOKIE_LEN_MAX failed
%{public}s %{public}s no other reference on socket, dumping backtrace:%{public}s
%{public}s %{public}s so->so_usecount <= 0, no backtrace
%{public}s called with null invalid len %d, backtrace limit exceeded
%{public}s nw_frame_create_external failed, dumping backtrace:%{public}s
%{public}s setsockopt TCP_ECN_MODE failed %{darwin.errno}d, no backtrace
%{public}s %{public}s tcp_set_read_timeout failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s invalid registration notification: %{public}s, no backtrace
%{public}s called with null other_protocol, dumping backtrace:%{public}s
%{public}s %{public}s TCP hlen %d segment length %d on %d buffers
%{public}s Assert inp->inp_flowhash != 0 failed
%{public}s %{public}s setting MSS to %d
%{public}s called with null len, backtrace limit exceeded
%{public}s %{public}s we asked for maximum %u frames, but got %u
%{public}s %{public}s flow is %{public}s
%{public}s Assert found_seg != NULL failed
%{public}s %{public}s no data to carry wake packet
%{public}s called with null globals, dumping backtrace:%{public}s
%{public}s %{public}s so=%p not a valid state =%x, backtrace limit exceeded
%{public}s failed to release inpcb reference, no backtrace
%{public}s ipi %p already in the list, no backtrace
%{public}s bytes_sacked (%u) can't be smaller than already SACKed segment length (%u), no backtrace
%{public}s Attempt to get segment-count on a chain-member, dumping backtrace:%{public}s
%{public}s %{public}s m is non-NULL but there is nothing to send so_snd.sb_mb %{public}s empty so_snd.sb_cc %u off %d len %d t_state[%{public}s], no backtrace
%{public}s %{public}s sbdrop - count not zero: len %d sb_cc %u
%{public}s %{public}s so=%p not a valid state =%x, dumping backtrace:%{public}s
%{public}s called with null protocol, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_MAXSEG failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_RXT_FINDROP failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s segmentation_offload_notification enabled
%{public}s flight_size (%d) can't be negative (snd_nxt:%u snd_max:%u, snd_una:%u, sacked:%u lost:%u retransmitted:%u)
%{public}s finalizer context has no buffer manager, but frame has buffer
%{public}s mach_timebase_info returned %u
%{public}s called with null context, backtrace limit exceeded
%{public}s called with null rt->rt_ifp
%{public}s called with null cookie, no backtrace
%{public}s called with null old_input_handler, no backtrace
%{public}s frame_array %p not empty, backtrace limit exceeded
%{public}s ipi %p already in the list, dumping backtrace:%{public}s
%{public}s nw_frame_create failed, backtrace limit exceeded
%{public}s called with null ret_frame_array, dumping backtrace:%{public}s
%{public}s get_remote_endpoint failed
%{public}s called with null len, dumping backtrace:%{public}s
%{public}s Attempt to set generation-count on a chain-member, no backtrace
%{public}s Assert tp->tentry.index == UTCPT_NONE || tp->tentry.mode > 0 failed
%{public}s called with null rt->rt_ifp, dumping backtrace:%{public}s
%{public}s %{public}s cc_algo %{public}s
%{public}s tcp_setsockopt TCP_CONNECTIONTIMEOUT failed %{darwin.errno}d
%{public}s %{public}s default_input_handler is different from the input_protocol
%{public}s %{public}s restarting TCP output on output available
%{public}s Protocol event reported for unknown address family %d
%{public}s %{public}s %{public}s: sb %p so %p cc %d mb %p, no backtrace
%{public}s %{public}s tcp_bind failed
%{public}s %{public}s tcp_set_keepalive failed %{darwin.errno}d, no backtrace
%{public}s %{public}s input available and we got %d frames
%{public}s register notification for %{public}s called with zero length, backtrace limit exceeded
%{public}s %{public}s t_pktlist is not empty in tcp_close, backtrace limit exceeded
%{public}s TCP route unusable
%{public}s %{public}s recv_bg: switching to %{public}s bg=%d recv_cc_algo=%u
%{public}s Attempt to get generation-count on a chain-member, dumping backtrace:%{public}s
%{public}s %{public}s tcp_set_enable_l4s failed %{darwin.errno}d, backtrace limit exceeded
%{public}s currently unsupported, no backtrace
%{public}s %{public}s failed to get tcp buffer in tcp-ip output
%{public}s %{public}s improperly called sodefunct, dumping backtrace:%{public}s
%{public}s %{public}s retransmit SYN %u
%{public}s %{public}s so %p [%d] usecount %d, backtrace limit exceeded
%{public}s nw_frame_create_external failed, backtrace limit exceeded
%{public}s called with null rt, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_NOTIMEWAIT failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s tcp_setsockopt TCP_RXT_CONNDROPTIME failed %{darwin.errno}d
%{public}s Assert tcp_tfo_halfcnt >= 0 failed
%{public}s %{public}s tcp_getlock: so=%p usecount=%x lrh= %{public}s, backtrace limit exceeded
%{public}s Bad link elm %p prev->next != elm, backtrace limit exceeded
%{public}s freed slab frame has unexpected buffer
%{public}s %{public}s apply socket parameters failed, dumping backtrace:%{public}s
%{public}s Assert (u_char *)lp - opt <= MAX_TCPOPTLEN failed
%{public}s %{public}s tcp_unlock: so=%p NO PCB usecount=%x lrh= %s, dumping backtrace:%{public}s
%{public}s %{public}s TCP listener failed to receive inbound connection within timeout, dropping connection, dumping backtrace:%{public}s
%{public}s mode %d schedtime %u runtime %u offset %u
%{public}s Underflow: %{public}s, decrement %llu, result %llu, dumping backtrace:%{public}s
%{public}s called with null path, dumping backtrace:%{public}s
%{public}s %{public}s new_frame has next, dumping backtrace:%{public}s
%{public}s %{public}s reassembled segment is wake packet
%{public}s %{public}s soclose: so=%p refcount=0
%{public}s no frame in frame array
%{public}s nw_frame_create failed, dumping backtrace:%{public}s
%{public}s called with null frame->finalizer
%{public}s nw_queue_context_create_source failed, no backtrace
%{public}s Protocol event reported for socket with faddr IN6ADDR_ANY
%{public}s mode %d schedtime %u runtime %u offset %u, deadline set to forever
%{public}s %{public}s tcp get heuristics failed
%{public}s tcp_rtlookup[6] failed
%{public}s %{public}s tcp_set_max_pacing_rate failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s bytes_lost (%u) can't be smaller than already lost segment length (%u)
%{public}s %{public}s tcp_lock: so=%p so_pcb=%p ref=%x lrh= %s, no backtrace
%{public}s len_added %u != len_to_add %u
%{public}s %{public}s Segment count is 0 for single-IP frame
%{public}s %{public}s UTCPT_KEEP: %u RTT_Cache: %{public}s, rtt_upd: %d, rtt: %u.%03ums, rtt_var: %u.%03ums rtt_nc: %u.%03ums, rtt_var_nc: %u.%03ums
%{public}s %{public}s NBIO not set, backtrace limit exceeded
%{public}s %{public}s computed sack_bytes_retransmitted (%d) not the same as cached value (%d)
%{public}s %{public}s read closed
%{public}s %{public}s is already connecting
%{public}s called with null (val != nil), dumping backtrace:%{public}s
%{public}s segment end(%u) can't be smaller than segment start(%u), dumping backtrace:%{public}s
%{public}s bytes_retransmitted (%u) can't be smaller than already retransmited segment length (%u), dumping backtrace:%{public}s
%{public}s %{public}s tcp_unlock: so=%p NO PCB usecount=%x lrh= %s
%{public}s %{public}s so=%p proto=%d couldn't set to STOPUSING, backtrace limit exceeded
%{public}s %{public}s tcp dispose
%{public}s called with null new_input_handler, dumping backtrace:%{public}s
%{public}s %{public}s t_state %{public}s
%{public}s Assert LIST_EMPTY(&tp->t_segq) failed
%{public}s %{public}s no other reference on socket
%{public}s Claiming bytes failed because start (%u) is beyond end (%u - %u)
%{public}s %{public}s output frame is no longer valid
%{public}s %{public}s queueing frame of length %u - fastpath
%{public}s %{public}s unable to copy frame for reassembly
%{public}s %{public}s failed to finalize tcp checksum, %s
%{public}s %{public}s SB_DROP not set
%{public}s Failed to extract data from frame, dumping backtrace:%{public}s
%{public}s called with null parameters, backtrace limit exceeded
%{public}s %{public}s tcp_setsockopt TCP_SENDMOREACKS failed %{darwin.errno}d, no backtrace
%{public}s bytes_lost (%u) and/or bytes_retransmitted (%u) can't be smaller than already lost/retransmitted segment length (%u), backtrace limit exceeded
%{public}s %{public}s sofree: not queued, no backtrace
%{public}s %{public}s improperly called sodefunct
%{public}s Copied %zu out of expected %u bytes, dumping backtrace:%{public}s
%{public}s called with null rt, no backtrace
%{public}s called with null tfo_cache_buffer, no backtrace
%{public}s Existing metadata %p doesn't match expected %p
%{public}s MTU reduced to %d\n
%{public}s %{public}s RELEASE pcb=%p so=%p usecount is negative, no backtrace
%{public}s invalid source frame, dumping backtrace:%{public}s
%{public}s nw_protocol_tcp_obj_alloc failed
%{public}s %{public}s tcp_set_enable_l4s failed %{darwin.errno}d, no backtrace
%{public}s tcp_trigger_connect failed %{darwin.errno}d, no backtrace
%{public}s %{public}s tcp_getlock: so=%p NULL so_pcb %{public}s, dumping backtrace:%{public}s
%{public}s %{public}s so->so_usecount <= 0, dumping backtrace:%{public}s
%{public}s inp %p invalid wantcnt %d no socket, dumping backtrace:%{public}s
%{public}s %{public}s apply socket parameters failed
%{public}s %{public}s tcp_set_no_push failed %{darwin.errno}d
%{public}s %{public}s tcp_setsockopt TCP_RXT_CONNDROPTIME failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt PERSIST_TIMEOUT failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s this should be handled by user_north_signal_error %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s m is non-NULL but there is nothing to send so_snd.sb_mb %{public}s empty so_snd.sb_cc %u off %d len %d t_state[%{public}s], dumping backtrace:%{public}s
%{public}s %{public}s sb=%p sb_flags=0x%x sb_so=%p usecount=%d, backtrace limit exceeded
%{public}s %{public}s tcp_disable_blackhole_detection(so) %{darwin.errno}d, backtrace limit exceeded
%{public}s tcp_get_southbound_frame failed %{darwin.errno}d, no backtrace
%{public}s %{public}s assertion failure SEQ_GEQ(tcp_hdr->th_ack, tp->snd_una) %u:%u tlen %u, flags=%{network:tcp_flags}x seq=%u, ack=%u, win=%u state=%{network:tcp_state}x rcv_nxt=%u, snd_una=%u, dumping backtrace:%{public}s
%{public}s Attempt to get segment-count on a chain-member, backtrace limit exceeded
%{public}s %{public}s NBIO not set
%{public}s failed to acquire inpcb reference, dumping backtrace:%{public}s
%{public}s failed to acquire inpcb reference, no backtrace
%{public}s %{public}s tcp_get_southbound_frame failed, socket is full minimum %u sbspace %u
%{public}s %{public}s nw_endpoint_get_address failed, no backtrace
%{public}s %{public}s tcp_set_read_timeout failed %{darwin.errno}d, no backtrace
%{public}s called with null other_protocol, no backtrace
%{public}s %{public}s this should be handled by user_north_signal_error %{darwin.errno}d, backtrace limit exceeded
%{public}s flight_size (%d) can't be negative (snd_nxt:%u snd_max:%u, snd_una:%u, sacked:%u lost:%u retransmitted:%u), dumping backtrace:%{public}s
%{public}s %{public}s setup state failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s ignoring wake low_water %u sb_cc %u
%{public}s %{public}s tcp_setsockopt TCP_NOTIMEWAIT failed %{darwin.errno}d, no backtrace
%{public}s Assert inp->inp_sndinprog_cnt-- > 0 failed
%{public}s %{public}s so_usecount %u so_state 0x%x
%{public}s %{public}s tcp_lock: so=%p so_pcb=%p ref=%x lrh= %s
%{public}s %{public}s so->so_usecount <= 0
%{public}s %{public}s inp_so->so_usecount(== %d) underflow  when removing timer entry, backtrace limit exceeded
%{public}s called with null object, no backtrace
%{public}s called with null (val != nil)
%{public}s segment %p[%u %u) was not inserted in the RB tree
%{public}s mode %d schedtime %u runtime %u new_runtime %u tcp_now %u offset %u, not pushing timer out
%{public}s invalid source frame, no backtrace
%{public}s %{public}s tcp_set_notsent_lowat failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s called with null val, dumping backtrace:%{public}s
%{public}s Segment ACKed list shouldn't contain any segments as they are removed immediately after being ACKed, backtrace limit exceeded
%{public}s %{public}s Sandbox does not allow __nexus_set_opt
%{public}s %{public}s segmentation offload notification not enabled
%{public}s called with null (val != nil), backtrace limit exceeded
%{public}s %{public}s is NULL
%{public}s called with null so, no backtrace
%{public}s %{public}s tcp_set_no_delay failed %{darwin.errno}d
%{public}s %{public}s tcp_setsockopt TCP_RXT_FINDROP failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s nw_protocol_notification_type_connection_idle is %{bool}d
%{public}s get_local_endpoint failed, dumping backtrace:%{public}s
%{public}s called with null tfo_cache_buffer
%{public}s called with null link_info, dumping backtrace:%{public}s
%{public}s called with null (len == sizeof(struct nw_link_congestion_info)), no backtrace
%{public}s Prague CC: Cubic origin point should be greater than 0
%{public}s %{public}s Segment count is 0 for single-IP frame, no backtrace
%{public}s end_offset %u != end_bytes %u
%{public}s %{public}s soclose: so=%p refcount=0, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_SENDMOREACKS failed %{darwin.errno}d, backtrace limit exceeded
%{public}s Invalid address family
%{public}s %{public}s ipv4 pcb local address lookup failed
%{public}s %{public}s soclose: usecount is zero so=%p, no backtrace
%{public}s %{public}s sb=%p sb_flags=0x%x sb_so=%p usecount=%d
%{public}s %{public}s sb=%p sb_flags=0x%x sb_so=%p usecount=%d, dumping backtrace:%{public}s
%{public}s Assert (sb->sb_flags & SB_LOCK) || (so->so_state & SS_DEFUNCT) || (so->so_flags1 & U_SOF1_DEFUNCTINPROG) failed
%{public}s dispatch_time: Integer overflow failed, backtrace limit exceeded
%{public}s %{public}s setup state failed %{darwin.errno}d
%{public}s %{public}s tcp_set_traffic_class failed %{darwin.errno}d, backtrace limit exceeded
%{public}s bytes_retransmitted (%u) can't be smaller than already retransmited segment length (%u)
%{public}s %{public}s ECONNRESET t_state %{public}s
%{public}s %{public}s rtt is %d - maxing it at 4 x MSL\n
%{public}s dispatch_time: Integer overflow failed, no backtrace
%{public}s get_remote_endpoint failed, dumping backtrace:%{public}s
%{public}s Existing metadata %p doesn't match expected %p, no backtrace
%{public}s %{public}s state is %{public}s
%{public}s %{public}s ECN flags (0x%x) not set correctly, no backtrace
%{public}s %{public}s soclose: NOFDREF, dumping backtrace:%{public}s
%{public}s called with null (buffer_size > 0), no backtrace
%{public}s called with null context
%{public}s %{public}s nw_protocol_tcp_set_connection_idle path is NULL
%{public}s bytes_retransmitted (%u) can't be smaller than already retransmited segment length (%u), no backtrace
%{public}s bytes_lost (%u) and/or bytes_retransmitted (%u) can't be smaller than already lost/retransmitted segment length (%u), no backtrace
%{public}s %{public}s computed sack hole not the same as cached value
%{public}s %{public}s tcp_setsockopt TCP_NOOPT failed %{darwin.errno}d, backtrace limit exceeded
%{public}s Assert pending_bytes > 0 failed
%{public}s called with null ecn_cache_buffer
%{public}s %{public}s tcp_set_notsent_lowat failed %{darwin.errno}d
%{public}s bytes_retransmitted (%u) can't be smaller than already retransmited segment length (%u), backtrace limit exceeded
%{public}s %{public}s state change to %{network:tcp_state}d
%{public}s %{public}s sending frame, %u:%u tlen %u flags=%{network:tcp_flags}x seq=%u, ack=%u, win=%u state=%{network:tcp_state}x rcv_nxt=%u, snd_una=%u svc %{public}s
%{public}s called with null path, backtrace limit exceeded
%{public}s %{public}s tcp_setsockopt TCP_NOOPT failed %{darwin.errno}d, no backtrace
%{public}s Assert tp->t_maxseg != 0 failed
%{public}s Prague CC: Cubic origin point should be greater than 0, no backtrace
%{public}s %{public}s is accepting an inbound connection
%{public}s bytes_retransmitted (%u) can't be smaller than retransmited segment length (%u)
%{public}s RB tree still contains segments while time ordered list is already empty, dumping backtrace:%{public}s
%{public}s currently not supported
%{public}s %{public}s buffer no longer valid
%{public}s %{public}s new_frame has next, backtrace limit exceeded
%{public}s %{public}s input protocol initiated disconnect
%{public}s Segment ACKed list shouldn't contain any segments as they are removed immediately after being ACKed, no backtrace
%{public}s %{public}s drop due to limit: seq %u rcv_nxt %u reqssqlen %u qlimit %u
%{public}s currently unsupported, backtrace limit exceeded
%{public}s called with null globals, backtrace limit exceeded
%{public}s called with null invalid len %d
%{public}s %{public}s tcp_set_traffic_class failed %{darwin.errno}d
%{public}s %{public}s tcp_set_background_management failed %{darwin.errno}d
%{public}s %{public}s failed to get output frames
%{public}s bytes_retransmitted (%u) can't be smaller than retransmited segment length (%u), dumping backtrace:%{public}s
%{public}s %{public}s inp_so->so_usecount(== %d) underflow  when removing timer entry
%{public}s Bad link elm %p prev->next != elm, dumping backtrace:%{public}s
%{public}s %{public}s pcb=%p release with zero count
%{public}s Invalid frame context %p
%{public}s %{public}s no mtu received
%{public}s called with null ecn_cache_buffer, dumping backtrace:%{public}s
%{public}s called with null len, no backtrace
%{public}s %{public}s tcp_setsockopt TCP_KEEPCNT failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s get_remote_endpoint failed, no backtrace
%{public}s %{public}s this should be handled by user_north_signal_error %{darwin.errno}d, no backtrace
%{public}s called with null ret_frame_array, backtrace limit exceeded
%{public}s get_remote_endpoint failed, backtrace limit exceeded
%{public}s %{public}s tcp_setsockopt TCP_RXT_CONNDROPTIME failed %{darwin.errno}d, backtrace limit exceeded
%{public}s tcp_setsockopt TCP_CONNECTIONTIMEOUT failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s called with null val, no backtrace
%{public}s Aggregate buffer length: %u sum: %u, backtrace limit exceeded
%{public}s %{public}s sofree: not queued, dumping backtrace:%{public}s
%{public}s source_offset < 0, backtrace limit exceeded
%{public}s tcp->release_is_delayed set during dispose
%{public}s tcp->release_is_delayed set during dispose, no backtrace
%{public}s %{public}s RST RLC compression: compressed %u RST segments [%hu:%hu]
%{public}s finalizer context has buffer manager, but frame has no buffer
%{public}s %{public}s tcp_set_no_delay failed %{darwin.errno}d, backtrace limit exceeded
%{public}s setsockopt SO_SNDLOWAT %u failed %{darwin.errno}d
%{public}s %{public}s tcp_finalize_send error %d for frame of length %u
%{public}s %{public}s tcp_getlock: so=%p NULL so_pcb %{public}s, backtrace limit exceeded
%{public}s start_offset %u != start_bytes %u
%{public}s flight_size (%d) can't be negative (snd_nxt:%u snd_max:%u, snd_una:%u, sacked:%u lost:%u retransmitted:%u), no backtrace
%{public}s failed to release inpcb reference, dumping backtrace:%{public}s
%{public}s %{public}s inp %p invalid wantcnt %d, so %p [%d] usecount %d retaincnt state 0x%x flags 0x%x, backtrace limit exceeded
%{public}s %{public}s RELEASE pcb=%p so=%p usecount is negative
%{public}s called with null invalid len %d, no backtrace
%{public}s get_remote_endpoint failed, no backtrace
%{public}s Unable to get path from input protocol, will not be able to get stats
%{public}s called with null cookie, backtrace limit exceeded
%{public}s %{public}s tcp_disable_blackhole_detection(so) %{darwin.errno}d, no backtrace
%{public}s %{public}s Ignoring wake low_water %u sbpace %u
%{public}s %{public}s got a connected event from the lower layer
%{public}s %{public}s tcp_set_read_timeout failed %{darwin.errno}d
%{public}s one RTT hasn't elapsed, not updating alpha
%{public}s %{public}s new_frame has next, no backtrace
%{public}s %{public}s EINVAL: optval %d t_maxseg %u tcp_minmss %d
%{public}s called with null tcp
%{public}s %{public}s tcp_setsockopt TCP_MAXSEG failed %{darwin.errno}d, no backtrace
%{public}s %{public}s tcp_set_notsent_lowat failed %{darwin.errno}d, backtrace limit exceeded
%{public}s not enough memory to allocate segment, disabling RACK
%{public}s %{public}s so_usecount %u t_state %u
%{public}s Attempt to get generation-count on a chain-member
%{public}s %{public}s sofree: not queued
%{public}s Bad link elm %p next->prev != elm
%{public}s %{public}s so=%p head still exist, no backtrace
%{public}s %{public}s so=%p not a valid state =%x
%{public}s %{public}s disconnect tcp
%{public}s %{public}s tcp_set_no_push failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s tcp_setsockopt TCP_RXT_FINDROP failed %{darwin.errno}d
%{public}s tcp_setsockopt TCP_CONNECTIONTIMEOUT failed %{darwin.errno}d, backtrace limit exceeded
%{public}s one RTT hasn't elapsed, not doing CWR
%{public}s %{public}s m is non-NULL but there is nothing to send so_snd.sb_mb %{public}s empty so_snd.sb_cc %u off %d len %d t_state[%{public}s], backtrace limit exceeded
%{public}s out_moved is %lu
%{public}s dispatch_time: Integer overflow failed, dumping backtrace:%{public}s
%{public}s nw_queue_context_create_source failed
%{public}s get_local_endpoint failed
%{public}s called with null handle, dumping backtrace:%{public}s
%{public}s %{public}s improperly called sodefunct, no backtrace
%{public}s %{public}s level %{public}s flow [TCP %{private}s:%d -> %{private}s:%d] is now defunct [rcv_fl 0x%x, snd_fl 0x%x]
%{public}s %{public}s so %p [%d] usecount %d, dumping backtrace:%{public}s
%{public}s Assert *free_frame_count >= 0 failed
%{public}s strict allocator failed
%{public}s called with null protocol, backtrace limit exceeded
%{public}s bytes_lost (%u) can't be smaller than already lost segment length (%u), no backtrace
%{public}s %{public}s chained frame len %u is smaller than TCP header size %u
%{public}s Bad link elm %p next->prev != elm, no backtrace
%{public}s source_offset < 0, dumping backtrace:%{public}s
%{public}s get_local_endpoint failed, backtrace limit exceeded
%{public}s %{public}s outaddr is NULL, backtrace limit exceeded
%{public}s called with null handle, backtrace limit exceeded
%{public}s %{public}s tcp_set_keepalive_interval failed %{darwin.errno}d
%{public}s TCP route unusable, no backtrace
%{public}s Assert SEQ_GEQ(tcp_hdr->th_ack, tp->snd_una) failed
%{public}s Assert SEQ_GEQ(snd_fack, s->rxmit) failed
%{public}s tcp get malloc failed for %u bytes
%{public}s %{public}s so %p [%d] usecount %d
%{public}s CCCryptorCreate
%{public}s %{public}s tfo preconnect
%{public}s Segment start (%u) is not same as retransmitted start sequence number (%u), backtrace limit exceeded
%{public}s %{public}s soclose: usecount is zero so=%p, backtrace limit exceeded
%{public}s inp %p invalid wantcnt %d no socket, no backtrace
%{public}s nw_frame_create_external failed
%{public}s tcp->release_is_delayed already set, no backtrace
%{public}s %{public}s TCP Packets:\n%{private,network:tcp_packets}.*P\n\tLast packet %ums ago.
%{public}s new CE count (%llu) can't be less than current CE count (%llu)OR newly ACKed (%llu) can't be less that current ACKed (%llu), dumping backtrace:%{public}s
%{public}s %{public}s assertion failure SEQ_GEQ(tcp_hdr->th_ack, tp->snd_una) %u:%u tlen %u, flags=%{network:tcp_flags}x seq=%u, ack=%u, win=%u state=%{network:tcp_state}x rcv_nxt=%u, snd_una=%u
%{public}s %{public}s It's a duplicate segment: tqe_seq %u tqe_len %u th_seq %u
%{public}s flight_size (%d) can't be negative (snd_nxt:%u snd_max:%u, snd_una:%u, sacked:%u lost:%u retransmitted:%u), backtrace limit exceeded
%{public}s get_local_endpoint failed, no backtrace
%{public}s called with null path
%{public}s %{public}s tcp_setsockopt TCP_SENDMOREACKS failed %{darwin.errno}d
%{public}s Old input handler does not match (%p != %p)
%{public}s %{public}s ECN flags (0x%x) not set correctly
%{public}s %{public}s m is non-NULL but there is nothing to send so_snd.sb_mb %{public}s empty so_snd.sb_cc %u off %d len %d t_state[%{public}s]
%{public}s %{public}s tcp_lock: so=%p so_pcb=%p ref=%x lrh= %s, dumping backtrace:%{public}s
%{public}s Assert ftc < SO_TC_STATS_MAX failed
%{public}s %{public}s waking the input_handler with %d bytes in our queue
%{public}s %{public}s tcp_set_fast_open_force_enable failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s Asked for min %u max %u bytes, max %u frames and got %d frames %u bytes, ret %u
%{public}s tcp_get_southbound_frame failed %{darwin.errno}d
%{public}s %{public}s link heuristics %{public}s
%{public}s %{public}s t_pktlist is not empty in tcp_close
%{public}s %{public}s t_pktlist is not empty in tcp_close, no backtrace
%{public}s Aggregate buffer length: %u sum: %u, no backtrace
%{public}s %{public}s inp %p invalid wantcnt %d, so %p [%d] usecount %d retaincnt state 0x%x flags 0x%x, dumping backtrace:%{public}s
%{public}s source buffer is no longer valid
%{public}s called with null parameters, dumping backtrace:%{public}s
%{public}s called with null context, dumping backtrace:%{public}s
%{public}s currently not supported, backtrace limit exceeded
%{public}s Assert tp->t_ccstate != NULL failed
%{public}s %{public}s first frame is wake packet
%{public}s %{public}s cc_algo %{public}s recvbg %d
%{public}s Failed to extract data from frame
%{public}s nw_frame_create failed
%{public}s %{public}s tcp_set_keepalive failed %{darwin.errno}d, backtrace limit exceeded
%{public}s called with null old_input_handler, backtrace limit exceeded
%{public}s %{public}s tcp_get_northbound_frame, returned NULL %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s currently unsupported
%{public}s %{public}s tcp_unlock: so=%p usecount=%x lrh= %s, no backtrace
%{public}s %{public}s so->so_usecount <= 0, backtrace limit exceeded
%{public}s ipi %p already in the list, backtrace limit exceeded
%{public}s Copied %zu out of expected %u bytes
%{public}s %{public}s nam is NULL, backtrace limit exceeded
%{public}s %{public}s tcp_set_keepalive failed %{darwin.errno}d
%{public}s %{public}s tcp_setsockopt PERSIST_TIMEOUT failed %{darwin.errno}d
%{public}s called with null (dscp_value <= _MAX_DSCP)
%{public}s setsockopt SO_SNDLOWAT %u failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s get_remote_endpoint failed, dumping backtrace:%{public}s
%{public}s called with null parameters
%{public}s %{public}s unknown protocol info type %d
%{public}s Segment start (%u) is not same as retransmitted start sequence number (%u), dumping backtrace:%{public}s
%{public}s %{public}s dropping tcp input frame since frame is no longer valid
%{public}s %{public}s no output frames len %d, TSO %d
%{public}s %{public}s set internet checksum offload failed (err %d)
%{public}s %{public}s tcp_unlock: so=%p usecount=%x lrh= %s, dumping backtrace:%{public}s
%{public}s %{public}s TCP listener failed to receive inbound connection within timeout, dropping connection, no backtrace
%{public}s %{public}s tcp_setsockopt TCP_MAXSEG failed %{darwin.errno}d
%{public}s %{public}s no path from input_handler received
%{public}s called with null new_input_handler
%{public}s setsockopt SO_RCVLOWAT %u failed %{darwin.errno}d
%{public}s Attempt to set generation-count on a chain-member
%{public}s %{public}s soclose: NOFDREF, backtrace limit exceeded
%{public}s %{public}s inp_so->so_usecount(== %d) underflow  when removing timer entry, no backtrace
%{public}s %{public}s tcp get heuristics failed, backtrace limit exceeded
%{public}s %{public}s tcp_setsockopt TCP_SENDMOREACKS failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_RXT_CONNDROPTIME failed %{darwin.errno}d, no backtrace
%{public}s called with null other_protocol, backtrace limit exceeded
%{public}s bytes_lost (%u) and/or bytes_retransmitted (%u) can't be smaller than already lost/retransmitted segment length (%u)
%{public}s currently unsupported, dumping backtrace:%{public}s
%{public}s %{public}s defunct flow error (%d)
%{public}s %{public}s defunct socket error (%d)
%{public}s %{public}s soclose: so=%p refcount=0, backtrace limit exceeded
%{public}s called with null rt
%{public}s called with null rt->rt_ifp, no backtrace
%{public}s %{public}s outaddr is NULL, no backtrace
%{public}s %{public}s tcp_set_no_push failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s tcp_trigger_connect failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s tcp_set_write_timeout failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s segment end(%u) can't be smaller than segment start(%u)
%{public}s bytes_lost (%u) and/or bytes_retransmitted (%u) can't be smaller than already lost/retransmitted segment length (%u), dumping backtrace:%{public}s
%s: pacer rate shouldn't be 0, CCA is %s (cwnd=%u, smoothed rtt=%u ms)
%{public}s called with null ecn_cache_buffer, backtrace limit exceeded
%{public}s %{public}s so_snd.sb_lowat %u sbspace %u
%{public}s %{public}s 
%{public}s %{public}s dropping input packet since frame is no longer valid
%{public}s %{public}s Segment count is 0 for single-IP frame, dumping backtrace:%{public}s
%{public}s %{public}s this should be handled by user_north_signal_error %{darwin.errno}d
%{public}s called with null cookie
%{public}s setsockopt TCP_ECN_MODE failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s Segment ACKed list shouldn't contain any segments as they are removed immediately after being ACKed, dumping backtrace:%{public}s
%{public}s new CE count (%llu) can't be less than current CE count (%llu)OR newly ACKed (%llu) can't be less that current ACKed (%llu), backtrace limit exceeded
%{public}s %{public}s chained frame len %u is smaller than TCP header size %u, backtrace limit exceeded
%{public}s Attempt to get segment-count on a chain-member
%{public}s %{public}s so=%p proto=%d couldn't set to STOPUSING, no backtrace
%{public}s %{public}s tcp_set_no_push failed %{darwin.errno}d, no backtrace
%{public}s %{public}s tcp_set_enable_l4s failed %{darwin.errno}d
%{public}s %{public}s tcp_setsockopt TCP_CONNECTIONTIMEOUT failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s strict_calloc(%zu, %zu) failed
%{public}s %{public}s cannot specify 0 as maximum_frame_count on a streaming socket
%{public}s %{public}s asked for min %u max %u bytes, max %u frames and got 1 frame of %u bytes on %p
%{public}s called with null other_protocol
%{public}s failed to release inpcb reference, backtrace limit exceeded
%{public}s %{public}s outaddr is NULL, dumping backtrace:%{public}s
%{public}s %{public}s tcp_set_no_delay failed %{darwin.errno}d, no backtrace
%{public}s %{public}s tcp_disable_blackhole_detection(so) %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s called with null old_input_handler
%{public}s tcp->release_is_delayed already set, dumping backtrace:%{public}s
%{public}s %{public}s tcp_get_northbound_frame, returned NULL %{darwin.errno}d
%{public}s %{public}s get_remote_endpoint failed
%{public}s %{public}s tcp_setsockopt PERSIST_TIMEOUT failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s get_remote_endpoint failed, backtrace limit exceeded
%{public}s %{public}s buffer smaller than tcp header
%{public}s %{public}s output buffer is no longer valid
%{public}s %{public}s soclose: usecount is zero so=%p
%{public}s %{public}s soclose: NOFDREF
%{public}s %{public}s TCP listener failed to receive inbound connection within timeout, dropping connection, backtrace limit exceeded
%{public}s called with null frame, backtrace limit exceeded
%{public}s called with null len
%{public}s called with null new_input_handler, no backtrace
%{public}s tcp_trigger_connect failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s bytes_sacked (%u) can't be smaller than already SACKed segment length (%u), dumping backtrace:%{public}s
%{public}s currently not supported, no backtrace
%{public}s Prague CC: Cubic origin point should be greater than 0, dumping backtrace:%{public}s
%{public}s new CE count (%llu) can't be less than current CE count (%llu)OR newly ACKed (%llu) can't be less that current ACKed (%llu), no backtrace
%{public}s CCCryptorUpdate
%{public}s %{public}s tcp_set_write_timeout failed %{darwin.errno}d, no backtrace
%{public}s Prague CC: Cubic origin point should be greater than 0, backtrace limit exceeded
%{public}s %{public}s failed to get tcp header
%{public}s %{public}s route is not usable: no checksum offload
%{public}s %{public}s level %{public}s flow is not eligible for defunct (%d)
%{public}s Invalid end coalesce timer
%{public}s nw_protocol_tcp_obj_alloc failed, backtrace limit exceeded
%{public}s called with null parameters, no backtrace
%{public}s tcp->release_is_delayed set during dispose, backtrace limit exceeded
%{public}s Existing metadata %p doesn't match expected %p, dumping backtrace:%{public}s
%{public}s %{public}s tcp_getlock: so=%p NULL so_pcb %{public}s
%{public}s currently in loss recovery, no need to do CWR
%{public}s Attempt to get generation-count on a chain-member, backtrace limit exceeded
%{public}s %{public}s %{public}s: sb %p so %p cc %d mb %p, dumping backtrace:%{public}s
%{public}s Underflow: %{public}s, decrement %llu, result %llu
%{public}s %{public}s send disconnect to input protocol
%{public}s %{public}s tcp_set_background_management failed %{darwin.errno}d, no backtrace
%{public}s tcp_setsockopt TCP_CONNECTIONTIMEOUT failed %{darwin.errno}d, no backtrace
%{public}s %{public}s flags=%{network:tcp_flags}x seq=%u, ack=%u, win=%u state=%{network:tcp_state}x rcv_nxt=%u, snd_una=%u
%{public}s Assert so->so_usecount > 0 failed
%{public}s %{public}s NBIO not set, no backtrace
%{public}s %{public}s ECN flags (0x%x) not set correctly, dumping backtrace:%{public}s
%{public}s inp %p invalid wantcnt %d no socket
%{public}s invalid source frame, backtrace limit exceeded
%{public}s called with null tfo_cache_buffer, backtrace limit exceeded
%{public}s %{public}s tcp_set_background_management failed %{darwin.errno}d, backtrace limit exceeded
%{public}s tcp->release_is_delayed already set, backtrace limit exceeded
%{public}s %{public}s assertion failure SEQ_GEQ(tcp_hdr->th_ack, tp->snd_una) %u:%u tlen %u, flags=%{network:tcp_flags}x seq=%u, ack=%u, win=%u state=%{network:tcp_state}x rcv_nxt=%u, snd_una=%u, backtrace limit exceeded
%{public}s Aggregate buffer length: %u sum: %u, dumping backtrace:%{public}s
%{public}s %{public}s SB_DROP not set, dumping backtrace:%{public}s
%{public}s returned frame array in slab is not empty
%{public}s globals: %p nw_context: %p identifier: %s
%{public}s %{public}s \n\t[%{public,uuid_t}.16P %{sensitive}s:%{public}d<->%{sensitive}s:%{public}d]\n\tInit: %d, Conn_Time: %u.%03ums, SYNs: %u, WR_T: %d/%d, RD_T: %d/%d, TFO: %d/%d/%d, ECN: %d/%d/%d, Accurate ECN (client/server): %s/%s, T
%{public}s called with null object
%{public}s called with null rt, backtrace limit exceeded
%{public}s %{public}s tcp_set_keepalive_idle_time failed %{darwin.errno}d, no backtrace
%{public}s tcp_get_southbound_frame failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s called with null (len == sizeof(struct nw_link_congestion_info)), dumping backtrace:%{public}s
%{public}s inp %p invalid wantcnt %d no socket, backtrace limit exceeded
%{public}s %{public}s probe connectivity %{public}s
%{public}s %{public}s frame no longer valid
%{public}s %{public}s sofree: not queued, backtrace limit exceeded
%{public}s %{public}s tcp_setsockopt TCP_NOOPT failed %{darwin.errno}d
%{public}s %{public}s so_rcv.sb_lowat %u sb_cc %u
%{public}s %{public}s tcp cache refcnt %d
%{public}s Assert SEQ_LEQ(ack, tp->snd_max) failed
%{public}s %{public}s so=%p not a valid state =%x, no backtrace
%{public}s %{public}s so=%p head still exist, dumping backtrace:%{public}s
%{public}s %{public}s RELEASE pcb=%p so=%p usecount is negative, dumping backtrace:%{public}s
%{public}s called with null ret_frame_array, no backtrace
%{public}s nw_queue_context_create_source failed, dumping backtrace:%{public}s
%{public}s %{public}s protocol upper layer initiated remove_input_handler
%{public}s invalid registration notification: %{public}s
%{public}s %{public}s frame is wake packet
%{public}s Frame cannot unclaim %u start bytes (has %u left)
%{public}s %{public}s probe connectivity enabled
%{public}s frame_array %p not empty, no backtrace
%{public}s Bad link elm %p prev->next != elm, no backtrace
%{public}s %{public}s pcb=%p release with zero count, no backtrace
%{public}s Copied %zu out of expected %u bytes, backtrace limit exceeded
%{public}s called with null old_input_handler, dumping backtrace:%{public}s
%{public}s %{public}s allowing read past connected state
%{public}s called with null val, backtrace limit exceeded
%{public}s Assert globals != NULL failed
%{public}s %{public}s soclose: usecount is zero so=%p, dumping backtrace:%{public}s
%{public}s %{public}s tcp_unlock: so=%p NO PCB usecount=%x lrh= %s, backtrace limit exceeded
%{public}s %{public}s so=%p proto=%d couldn't set to STOPUSING, dumping backtrace:%{public}s
%{public}s failed to acquire inpcb reference, backtrace limit exceeded
%{public}s called with null so, backtrace limit exceeded
%{public}s nw_protocol_tcp_obj_alloc failed, no backtrace
%{public}s nw_endpoint_get_address failed
%{public}s %{public}s \n\t[%{public,uuid_t}.16P %{public}s:%{public}d<->%{public}s:%{public}d]\n\tInit: %d, Conn_Time: %u.%03ums, SYNs: %u, WR_T: %d/%d, RD_T: %d/%d, TFO: %d/%d/%d, ECN: %d/%d/%d, Accurate ECN (client/server): %s/%s, TS: %d,
%{public}s %{public}s frame marks connection complete, marking output finished
%{public}s %{public}s Protocol event %d=%d
%{public}s %{public}s read timeout
%{public}s %{public}s no input handler
%{public}s Segment start (%u) is not same as retransmitted start sequence number (%u)
%{public}s TCP route unusable, dumping backtrace:%{public}s
%{public}s %{public}s chained frame len %u is smaller than TCP header size %u, dumping backtrace:%{public}s
%{public}s Attempt to get segment-count on a chain-member, no backtrace
%{public}s Assert !(so->so_flags & SOF_MP_SUBFLOW) || (so->so_snd.sb_flags & SB_NOCOMPRESS) failed
%{public}s %{public}s SB_DROP not set, no backtrace
%{public}s invalid source frame
%{public}s Failed to extract data from frame, backtrace limit exceeded
%{public}s failed to get tcp frame array
%{public}s %{public}s tcp_bind failed, backtrace limit exceeded
%{public}s called with null object, backtrace limit exceeded
%{public}s RB tree still contains segments while time ordered list is already empty, no backtrace
%{public}s called with null context, no backtrace
%{public}s %{public}s nam is NULL
%{public}s %{public}s outaddr is NULL
%{public}s setsockopt SO_SNDLOWAT %u failed %{darwin.errno}d, no backtrace
%{public}s %{public}s ipv6 pcb local address lookup failed
%{public}s %{public}s dropping connection on 2 MSL timeout
%{public}s Bad link elm %p next->prev != elm, dumping backtrace:%{public}s
%{public}s %{public}s notifying segmentation offload value %d
%{public}s called with null path, no backtrace
%{public}s %{public}s tcp_set_keepalive failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s %{public}s tcp_set_read_timeout failed %{darwin.errno}d, backtrace limit exceeded
%{public}s invalid registration notification: %{public}s, dumping backtrace:%{public}s
%{public}s called with null (len == sizeof(struct nw_link_congestion_info)), backtrace limit exceeded
%{public}s Protocol event reported for socket with faddr INADDR_ANY
%{public}s %{public}s tcp get heuristics failed, dumping backtrace:%{public}s
%{public}s called with null so, dumping backtrace:%{public}s
%{public}s segment end(%u) can't be smaller than segment start(%u), no backtrace
%{public}s %{public}s offset does not make any sense: %u
%{public}s %{public}s queueing frame of length %u - slowpath
%{public}s %{public}s %{public}s: sb %p so %p cc %d mb %p, backtrace limit exceeded
%{public}s %{public}s pcb=%p so=%p usecount is negative, no backtrace
%{public}s called with null cookie, dumping backtrace:%{public}s
%{public}s %{public}s tcp_setsockopt TCP_RXT_FINDROP failed %{darwin.errno}d, no backtrace
%{public}s called with null (dscp_value <= _MAX_DSCP), backtrace limit exceeded
%{public}s register notification for %{public}s called with zero length, dumping backtrace:%{public}s
%{public}s Assert sb->sb_wantlock != 0 failed
%{public}s Assert so_valid_tc(sotc) failed
%{public}s Assert tp->t_pmtud_saved_maxopd > 0 failed
%{public}s Invalid flags %u %u %u
%{public}s %{public}s tcp_set_background_management failed %{darwin.errno}d, dumping backtrace:%{public}s
%{public}s setsockopt SO_SNDLOWAT %u failed %{darwin.errno}d, backtrace limit exceeded
%{public}s Assert tp != NULL failed
%{public}s %{public}s retransmit%{public}s seq=%u %u
%{public}s %{public}s TCP listener failed to receive inbound connection within timeout, dropping connection
%{public}s mode %d schedtime %u runtime %u tcp_now %u drift %d / offset %d
%{public}s Assert inp->inp_pcbinfo->ipi_twcount != 0 failed
%{public}s nw_frame_create_external failed, no backtrace
%{public}s invalid registration notification: %{public}s, backtrace limit exceeded
%{public}s Segment start (%u) is not same as retransmitted start sequence number (%u), no backtrace
%{public}s %{public}s couldn't allocate memory for struct tseg_qent
%{public}s %{public}s inp == NULL || so->so_pcb == NULL
%{public}s %{public}s append frame count %u length %u sb_cc %u
%{public}s Assert is_incr == false failed
%{public}s called with null frame, dumping backtrace:%{public}s
%{public}s Assert globals->free_frame_count > 0 failed
%{public}s %{public}s tcp_setsockopt PERSIST_TIMEOUT failed %{darwin.errno}d, no backtrace
%{public}s %{public}s traffic_mgmt_background current %d new %d
%{public}s called with null (len == sizeof(bool)), dumping backtrace:%{public}s
%{public}s %{public}s tcp_set_max_pacing_rate failed %{darwin.errno}d
%{public}s %{public}s no other reference on socket, backtrace limit exceeded
%{public}s %{public}s tcp_bind failed, no backtrace
%{public}s setsockopt TCP_ECN_MODE failed %{darwin.errno}d, backtrace limit exceeded
%{public}s %{public}s tcp_set_max_pacing_rate failed %{darwin.errno}d, no backtrace
%{public}s currently not supported, dumping backtrace:%{public}s
%{public}s %{public}s soclose: so=%p refcount=0, no backtrace
%{public}s %{public}s inp_so->so_usecount(== %d) underflow  when removing timer entry, dumping backtrace:%{public}s
%{public}s called with null frame->finalizer, no backtrace
%{public}s called with null so
%{public}s dispatch_time: Integer overflow failed
%{public}s %{public}s socket inpcb is NULL
%{public}s %{public}s nw_endpoint_get_address failed, backtrace limit exceeded
%{public}s segment end(%u) can't be smaller than segment start(%u), backtrace limit exceeded
%{public}s %{public}s tcp pcb is NULL
%{public}s %{public}s tcp_setsockopt TCP_MAXSEG failed %{darwin.errno}d, backtrace limit exceeded
%{public}s called with null rt->rt_ifp, backtrace limit exceeded
%{public}s register notification for %{public}s called with zero length, no backtrace
%{public}s %{public}s invalid checksum
%{public}s %{public}s tcp_lock: so=%p so_pcb=%p ref=%x lrh= %s, backtrace limit exceeded
%{public}s called with null globals
%{public}s nw_frame_create failed, no backtrace
%{public}s Assert globals->free_slab_frame_count >= 0 failed
%{public}s %{public}s inp %p invalid wantcnt %d, so %p [%d] usecount %d retaincnt state 0x%x flags 0x%x
%{public}s called with null (max_frame_count > 0), no backtrace
%{public}s %{public}s skipping
%{public}s called with null (len == sizeof(bool))
%{public}s bytes_retransmitted (%u) can't be smaller than retransmited segment length (%u), backtrace limit exceeded
%{public}s Assert SLIST_EMPTY(&tp->t_notify_ack) failed
%{public}s %{public}s copy from snd buffer to channel buffer failed
%{public}s %{public}s recv_bg: reactive teardown (recv_bg_viable=%d algo_mismatch=%d active=%u desired=%d)
%{public}s called with null protocol
%{public}s called with null ecn_cache_buffer, no backtrace
%{public}s %{public}s tcp_setsockopt TCP_CONNECTIONTIMEOUT failed %{darwin.errno}d, backtrace limit exceeded
%{public}s called with null val
%{public}s called with null (val != nil), no backtrace
%{public}s %{public}s tcp_getlock: so=%p usecount=%x lrh= %{public}s, dumping backtrace:%{public}s
%{public}s RB tree still contains segments while time ordered list is already empty, backtrace limit exceeded
%{public}s frame_array %p not empty
%{public}s %{public}s so=%p proto=%d couldn't set to STOPUSING
%{public}s %{public}s skipping so %p SS_NOFDREF
%{public}s called with null tcp, backtrace limit exceeded
%{public}s called with null link_info, backtrace limit exceeded
%{public}s %{public}s tcp_set_keepalive_interval failed %{darwin.errno}d, no backtrace
%{public}s %{public}s state change to %{public}s
%{public}s %{public}s queueing frame %p of length %u
tcp_compute_segment_length
ip_ctloutput
tcp_add_accecn_option
tcp_cubic_init
tcp_nocopy
SYN_RCVD
set_tcp_stream_priority
tcp_close_locked
tcp_process_timerlist
nw_protocol_tcp_timer_init
__nw_protocol_tcp_disconnect_block_invoke
nw_proto_tcp_route_init
tcp_seg_len
tcp_segs_clear_sacked
tcp_usr_rcvoob
__nw_frame_effective_length
__nw_frame_unclaimed_bytes
nw_protocol_tcp_finalize_output_frames_block_invoke
tcp_ctlinput
in_pcbinfo_attach
tcp_mtudisc
sbcompress
tcp_run_conn_timer
tcp_xmit_timer
nw_protocol_tcp_disconnected
nw_protocol_tcp_error
tcp_get_northbound_frames
av
socket_post_kev_msg_closed
nw_protocol_tcp_get_slab_frame_block_invoke
nw_protocol_tcp_get_malloc_frame
prague_update_alpha
sbdrop
FIN_WAIT_2
tcp_mss
tcp_heuristic_tfo_rst
tcp_cubic_cwnd_init_or_reset
tcp_rbbr_switch_to
tcp_drop
tcp_seg_alloc_init
tcp_seg_rto_insert_end
tcp_output_batch_acks_begin
set_frame_service_class
tcp_run_timerlist
nw_protocol_tcp_get_buffer_manager_malloc_frame
nw_protocol_tcp_wake_connected
nw_protocol_tcp_dispose
__nw_frame_collapse
tcp_lock
microuptime_ns
sodefunct
oam
 SYN
nw_protocol_tcp_disconnect
FIN_WAIT_1
tcp_prague_init
tcp_output
true
tcp_heuristic_ecn_droprst
__nw_protocol_tcp_create
nw_protocol_tcp_get_message_properties
tcp_usr_send
not
so_throttle_best_effort
packet_service_class_to_str
so_tc_update_stats
nw_frame_tcp_finalize
nw_tcp_access_context
__nw_frame_array_claim
__nw_frame_claim_internal
nw_proto_tcp_tfo_cookie_len
tcp_rack_free_and_disable
tcp_heuristic_ecn_synrst
nw_protocol_tcp_connected
tcp6_connect
__nw_frame_set_compression_generation_count
false
nw_protocol_tcp_get_path_is_viable
unregistered
LISTEN
tcp_set_recv_bg
tcp_heuristic_tfo_loss
user_north_signal_error
nw_protocol_tcp_release
nw_protocol_tcp_remove_input_handler
tcp_segs_doack
tcp_release_route_heuristics
aes_encrypt_cbc
nw_protocol_tcp_input_available
nw_protocol_tcp_get_output_frames
so
tcp_disconnect
bk
nw_protocol_tcp_signal_error
nw_protocol_tcp_set_no_push
inp_flush
sbunlock
tcp_heuristics_cache_init
tcp_cubic_after_timeout
nw_proto_tcp_tfo_get_cookie
nw_protocol_tcp_connect
tcp_mark_seg_lost
ctl
in_pcb_checkstate
nw_protocol_tcp_set_send_low_water_mark
ip6_ctloutput
marked as
process
nw_protocol_tcp_wake_disconnected
nw_proto_tcp_bind
nw_protocol_tcp_set_receive_low_water_mark
nw_protocol_tcp_set_max_pacing_rate
__nw_frame_is_single_ip_aggregate
is already
syscall-unix
nw_protocol_tcp_copy_info
tcp_timers
tcp_tfo_rcv_probe
in_pcbremlists
nw_protocol_tcp_copy_flow_registration
__nw_frame_uses_external_data
v16@?0^{ifnet_stats_per_flow=QQQIIIIIIIIIIIIIIIIIIb1b1b1b1b1b1b1b1b1b1b6SIQQQQ}8
tcp_handle_msgsize
tcp_connect
none
tcp_get_route_heuristics
in_pcbdetach
nw_protocol_tcp_get_frame_count
CLOSED
tcp_getlock
tcp_segs_sent_clean
tcp_clear_recv_bg
inp_fc_unthrottle_tcp
sblock
kernel
nw_protocol_timer_run_inner
nw_protocol_tcp_wake_write_timeout
nw_proto_tcp_notify_segmentation_offload
nw_protocol_tcp_set_connection_idle
tcp_prague_after_timeout
tcp_fill_info
frame->aggregate_buffer_length
nw_protocol_tcp_get_slab_frame
nw_protocol_tcp_finalize_output_frames
defunct
sosendcheck
unknown
__nw_frame_buffer_used_malloc
nw_protocol_tcp_wake_write_timeout_block_invoke
tcp_close
tcp_seg_mark_sacked
nw_protocol_tcp_wake_keepalive_block_invoke
inp
__nw_protocol_tcp_disconnect
tcp_attach
update_cwnd
invalid
tcp_usr_connect
tcp_input_carry_wake_packet
tcp_prague_process_ecn
__nw_frame_unclaim_internal
tcp_sched_timerlist
in_pcbdispose
nw_protocol_tcp_copy_frame
nw_tcp_init_globals
nw_protocol_tcp_update_metadata
enabled
nw_protocol_tcp_reset_keepalives
CLOSE_WAIT
tcp_respond
nw_protocol_tcp_notify
tcp_set_new_cc
tcp_connection_fill_info
tcp_sack_doack
sbflush
be
tcp_remove_timer
tcp[%llu]
__nw_frame_get_segment_count
tcp_garbage_collect
tcp_heuristic_tfo_middlebox
nw_frame_tcp_finalize_block_invoke
microuptime
Network
nw_proto_tcp_ecn_enabled
nw_protocol_tcp_replace_input_handler
nw_protocol_tcp_register_notification
buffer_manager_use_malloc
prague_cwr
tcp_flight_size
nw_proto_tcp_ecn_update_cache
sosetdefunct
tcp_input_available
tcp_unlock
__nw_frame_finalize
tcp_set_lotimer_index
tcp_heuristic_ecn_loss
tcp_pacer_get_packet_interval
nw_protocol_tcp_output_finished
ESTABLISHED
nw_protocol_tcp_get_external_frame
aes_encrypt_key128
nw_protocol_tcp_get_all_stats
nw_protocol_tcp_apply_parameters
tcp_seg_sent_insert_before
tcp_ctloutput
tcp6_usr_connect
tcp_heuristic_ecn_aggressive
nw_protocol_tcp_wake_keepalive
nw_protocol_tcp_link_state
com.apple.network.tcp
nw_protocol_tcp_wake_read_timeout_block_invoke
tcp_prague_cwnd_init_or_reset
tcp_sack_detect_reordering
process_suspended
add_to_time_wait_locked
inp_fc_feedback
nw_protocol_tcp_updated_path
nw_protocol_tcp_unregister_notification
SYN_SENT
CLOSING
tcp_trigger_connect
off
tcp_cubic_update
__nw_frame_set_metadata
nw_protocol_tcp_get_send_buffer_size
LAST_ACK
tcp_heuristics_cache_destroy
__nw_frame_check_validity
vo
tcp_sched_timers
nw_protocol_tcp_initialize_inbound
tcp_init
tcp_seg_sent_insert
tcp_seg_delete_acked
nw_protocol_tcp_copy_frame_to_buffer
tcp_rbbr_init
nw_protocol_tcp_signal_error_block_invoke
nw_protocol_tcp_get_input_frames
tp
is
nw_tcp_access_globals
nw_protocol_tcp_input_flush
nw_protocol_tcp_reset
nw_protocol_tcp_set_no_delay
tcp_ip_output_send_block_invoke
sofreelastref
tcp_coalesce_timer_updates_end
tcp_sackhole_alloc
v8@?0
nw_protocol_tcp_wake_send_block_invoke
TIME_WAIT
tcp_usr_abort
tcp_ip_output_send
sig
nw_protocol_tcp_output_available
tcp_usrclosed
__nw_frame_unclaimed_length
B16@?0^{nw_frame={os_object_header_s=^vii}{?=^{nw_frame}^^{nw_frame}}{?=^{nw_frame}^^{nw_frame}}IIII{?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}^?^v^{dispatch_data_s}^{nw_mem_buffer_manager}*{nw_frame_protocol_metadata={?
__nw_frame_set_external_data
nw_protocol_tcp_initialize
in_pcbladdr
nw_protocol_tcp_add_input_handler
nw_protocol_tcp_get_receive_buffer_size
tcp_input
vi
tcp_get_heuristics
nw_protocol_tcp_wake_read_timeout
disabled
nw_proto_tcp_tfo_update_cache
tcp_rxtseg_insert
tcp_add_notify_ack_marker
__nw_frame_set_is_wake_packet
on
rd
nw_protocol_tcp_set_no_wake_from_sleep
tcp_reass
tcp_output_batch_acks_end
tcp_sack_output
soclose_wait_locked
__nw_frame_buffer_get_manager
sb_empty_assert
nw_protocol_tcp_log_summary
__nw_frame_get_ecn_flag
tcp_cubic_post_fr
nw_proto_tcp_tfo_enabled
tcp_tfo_synack
rv
tcp_pmtud_revert_segment_size
nw_protocol_tcp_wake_read_closed_block_invoke
__nw_frame_set_dscp_value
nw_protocol_tcp_waiting_for_output
tcp_rst_rlc_compress
cubic_target
__nw_frame_get_compression_generation_count
user_tcp_init_all_block_invoke
bk_sys
nw_protocol_tcp_wake_read
tcp_notify
```
