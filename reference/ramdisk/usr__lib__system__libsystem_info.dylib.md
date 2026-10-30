# `/usr/lib/system/libsystem_info.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 364,720 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 37 (Size: 3320)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (18)

- `/usr/lib/system/libsystem_info.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libsystem_asl.dylib (compatibility version 1.0.0, current version 409.40.3)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libsystem_dnssd.dylib (compatibility version 1.0.0, current version 3111.40.45)`
- `/usr/lib/system/libsystem_notify.dylib (compatibility version 1.0.0, current version 368.40.2)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`
- `/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15)`
- `/usr/lib/system/libsystem_darwin.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libsystem_featureflags.dylib (compatibility version 1.0.0, current version 111.0.0)`
- `/usr/lib/system/libsystem_darwindirectory.dylib (compatibility version 1.0.0, current version 1.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (437)

```
rpc
Invalid value for ai_flags
0
;; [%s type %d class %d] timeout [ctx %p %p]\n
alias
service
mac
rc >= 1
No address associated with nodename
getpwuid
getgrgid
;; DNSServiceProcessResult -> %d\n
;; mdns_item_call %s type %u class %u\n
\t: 
mobile
uid
_analyticsusers
%s: 
; s1 = %u, s2 = %u
;; new timeout [%s type %d class %d] (waiting for AAAA) %ld.%ld [ctx %p %p]\n
user
svcudp_create - cannot getsockname
xdr_reference: out of memory
.rhosts lstat failed
%s%02x
GOT_ERROR
getaddrinfo
%s_%s
Database is busy
yp_match: clnt_call
RPC: Failed (unspecified error)
pmap_getmaps rpc problem
svcudp_create: socket creation problem
L4488s*4s
L4488sssss44
.e.f.ip6.arpa
network
Bad hints
com.apple.system.info:%s
servname not supported for ai_socktype
yp_master: clnt_call
RPC: Can't encode arguments
Request arguments bad
B24@?0Q8^v16
.rhosts fstat failed
;; mdns is_complete type %d ctx %p host addr count %d complete -> true\n
netgroup
/var/run/ypbind.lock
No such map in server's domain
getpwnam
pw_name
RPC: Authentication error
,
/dev/
%x:%x:%x:%x:%x:%x
;; _mdns_search calling DNSServiceProcessResult\n
reqtype
Invalid server verifier
L4488ss44LssssL
muser
;; [%s type %hu class %hu]: malformed reply [ctx %p]\n
;; mdns is_complete unexpected type %d ctx %p\n
si_item_retain
search
;; mdns is_complete type %d ctx %p %scomplete\n
default
com.apple.access_%s
procname
/var/empty
svc_run: - select failed
/etc/ethers
;; initialization error %d\n
authunix_create: out of memory\n
connect to address %s: 
Host name lookup failure
;; DNSServiceProcessResult status %d [ctx %p %p]\n
Memory allocation failure
cache_set: victim not found
/.rhosts
cache
/etc/master.passwd
;; [%s type %d class %d] continuing ctx %p\n
;; _mdns_query_callback ctx %p flags=0x%08x%s\n
;; mdns is_complete type %d ctx %p host name %s complete -> true\n
v24@?0^{darwin_directory_record_s=CI*[16C]BS(?={?=I***}{?=^*})}8^B16
Failed to allocate memory for a uuid
si_destination_compare
0%x
YP server for domain %s not responding, still trying\n
Failed to re-allocate memory for the group list
%s: %s\n
.rhosts not regular file
bad .rhosts owner
Unknown resolver error
v8@?0
tcp
/etc/fstab
Address family for nodename not supported
pw_passwd
Can't communicate with portmapper
_accessory_mobile_share
; low version = %u, high version = %u
protocol
ai_family not supported
*
; why = 
cache_set: victim alloc failed
cache_file
file
;; _mdns_sdref is NULL, initialize = true\n
;; [%s type %hu class %hu]: name mismatch [ctx %p]\n
com.apple.network.libinfo
xdr_string: out of memory
rcmd: write (setting up stderr): %s\n
si_list_release
yp_first: clnt_call
RPC: Unknown protocol
xdrrec_create: out of memory
/etc/hosts.equiv
Local domain name not set
L4488s*44c
vfs.generic.apfs.edt_fstab
ai_protocol not supported
Cannot receive reply to broadcast
%s%s
/Library/Managed Preferences/mobile
Success
com.apple.system.libinfo.muser
/dev/random
broadcast: ioctl (get interface flags)
/
%d
DarwinDirectory
;; [%s type %hu class %hu] reply [ctx %p]\n
Failed to allocate memory for a compatibility uid/gid
L4488s4@
;; kevent m=%d ev.filter=0x%08x\n
;; [%s type %d class %d] finished processing ctx %p\n
;; _mdns_hostent_append_alias(%p, %s)\n
self.thread.%lu
\n
;; _mdns_query_callback sending kevent wakeup\n
darwin_directory
%hu
Local resource allocation failure
 \t
@
LibinfoLookups
localhost
%s/%s.%s
username
; errno = %s
rcmd: %s: %s\n
 %x:%x:%x:%x:%x:%x
clntudp_create
getgrouplist
Server rejected credential
/etc/hosts
 - 
%s.%s
No such key in map
(null)
L4488222s
YP unknown error %d\n
version
svcudp_create: out of memory\n
Unknown host
;; new timeout [%s type %d class %d] (waiting for more) %ld.%ld [ctx %p %p]\n
udp
L448844444Ss
link#%d
%s/%s.plist
L4488s4*4
;; mdns_hostbyname %s type %u class %u\n
;; ctx %d %p error=%d complete=%s\n
/etc/protocols
;; mdns_hostbyaddr %s type %u class %u\n
group
Server rejected verifier
false
;; mdns is_complete type %d ctx %p srv %p complete -> true\n
YP server error
YES
pw_shell
Client credential too weak
cache_set: could not allocate new rpc_buffer
;; set kevent timeout %ld.%ld [ctx %p %p]\n
;; [%s type %hu class %hu]: error %d [ctx %p]\n
/etc/sysinfo.conf
nodename nor servname provided, or not known
Can't communicate with ypbind
select: protocol failure in circuit setup\n
/etc/rpc
;; [%s type %hu class %hu]: insufficient buffer space for reply [ctx %p]\n
RES_DEBUG
RPC failure
0123456789abcdef
so
Trying %s...\n
.rhosts writeable by other than owner
%u
;; mdns_srv_byname %s type %u class %u\n
%s%%%s
RPC: Procedure unavailable
L4488ss
host
clnttcp_create
/etc/group
L4488ss4*
;; _mdns_search exit res %d\n
;; mdns query %s type %d class %d ifindex %d [ctx %p]\n
;; kevent EV_TRIGGER: %s [ctx %p]\n
%u.%u.%u.%u.in-addr.arpa.
0.0.0.0
clnttcp_create failed
;; [%s type %hu class %hu] cname %s [ctx %p]\n
yp_next: clnt_call
gr_name
Error %d
RPC: Program/version mismatch
Failed to allocate memory for the group list
Broadcast select problem
rcmd: getaddrinfo: %s\n
SYSINFO_CONF_ENABLE
si_item_release
yp_maplist: clnt_call
RPC: Program not registered
Cannot create socket for broadcast rpc
%s%s/%s.plist
: 
L4488sss
addrinfo
yp_order: clnt_call
Invalid client verifier
com.apple.netsrc
;; _mdns_hostent_append_addr(%p, %p, %u)\n
si_list_retain
/usr/bin/false
RPC: Unable to send
Invalid client credential
Unknown error
127.0.0.1
Can't bind to server which serves this domain
pw_gid
 %x:%x:%x:%x:%x:%x %s
/etc/passwd
L4488s*44
rw
;; _mdns_search overall %scomplete\n
Darwin Directory unable to look up multiuser config flags
XBS_DISABLE_LIBINFO
gr_members
gid
No address associated with name
/etc/aliases
;; finished _mdns_search loop [ctx %p %p]\n
%s
RPC: Can't decode result
/var/run/portmap.socket
xdr_array: out of memory
rcmd: accept: %s\n
%sip6.arpa.
YP server version mismatch - server can't supply service.
query
Resolver Error 0 (no error)
;; [%s type %d class %d] done [ctx %p %p]\n
;; [%s type %hu class %hu]: malformed reply (too small) [ctx %p]\n
pw_dir
B24@?0r*8^v16
broadcast: ioctl (get interface configuration)
Unknown server error
Resolver internal error
/etc/netgroup
/etc/services
Failed to allocate memory for a uid/gid
svc_tcp: makefd_xprt: out of memory\n
rcmd: too many files\n
/root
groupname
RPC: Timed out
RPC: Program unavailable
Failed (unspecified error)
/smx7MYTQIi2M
Cannot send broadcast packet
Server data base is bad
mdns
r
;; DNSServiceProcessResult error status %d [ctx %p %p]\n
;; mdns_addrinfo node %s serv %s\n
ai_socktype not supported
?
(unknown authentication error - %d)
L4488s*4
;; _mdns_search ctx %p %scomplete\n
 - in
init
/usr/lib/info
RPC: (unknown error code)
RPC: Incompatible versions of RPC
RPC: Port mapper failure
si_data.c
No more records in map database
auth_none.c - Fatal marshalling problem
RPC: Success
RPC: Server can't decode arguments
rcmd: socket: All ports in use\n
rcmd: socket: %s\n
socket: protocol failure in circuit setup.\n
in
;; mdns is_complete ctx %p type mismatch (%d != %d) - incomplete\n
nameinfo
RPC: Remote system error
Authentication OK
clnt_raw.c - Fatal header serialization error.
svctcp_.c - udp socket creation problem
svctcp_.c - cannot getsockname or listen
grouplist
fcntl: F_SETFD
Can't communicate with ypserv
pw_uid
gr_gid
RPC: Unable to receive
svctcp_create: out of memory\n
 (kDNSServiceFlagsMoreComing is set)
;; cleared kDNSServiceFlagsMoreComing flag for ctx %p\n
%x
si_destination_compare_no_dependencies
Cannot set socket option SO_BROADCAST
true
rc >= 0
com.apple.system.config.network_change
Access violation
RPC: Unknown host
/etc/networks
:
L4488@@
Temporary failure in name resolution
Non-recoverable failure in name resolution
Failed to allocate memory for a compatibility user uuid
available
;; _mdns_search wait loop\n
;; kevent wakeup\n
;; type ns_t_a got_a_response=%s ctx %p\n
argument buffer overflow
::1
/usr/lib/libnetwork.dylib
%s:%s:%s:%s:%s:%s
Failed to allocate memory for a compatibility group uuid
L4488s*44a
;; mdns is_complete type %d ctx %p clear more coming - complete\n
close
getgrnam
%s\n
xdr_bytes: out of memory
rcmd: select (setting up stderr): %s\n
com.apple.system.notify.service.path:0x87:
GOT_DATA
;; mdns is_complete type %d ctx %p more coming - incomplete\n
System error
connect(%d, ...) ctl_id=%u, failed: %m
libnetwork.dylib did not set path_check
ND Rule 6, prefer d2, d2 precedence %d > d1 precedence %d
Rule 3, prefer d2, d1 source is deprecated
kvbuf_add_val_len: overflow when adding sizeof(uint32_t) (%zu) and len (%u)
Warning: Libinfo call to mDNSResponder on main thread
ND Rule 6, prefer d1, d1 precedence %d > d2 precedence %d
si_destination_lookup for dst1 failed
calloc(%zu) failed: %m
prefering 1, dst1 min rtt %f < dst2 min rtt %f, leeway %u small leeway %u
prefering 1 slightly, dst1 min rtt %f < dst2 min rtt %f, leeway %u small leeway %u
prefer dst 1, dst 2 is p2p, dst 1 is not
_muser_call: Failure (%d) with retry, bailing
%{public}s dst1 is NULL
ND Rule 8, prefer d1, d1 scope %d < d2 scope %d
ND Rule 8, prefer d2, d2 scope %d < d1 scope %d
prefering 2 slightly, dst1 min rtt %f > dst2 min rtt %f, leeway %u small leeway %u
prefer 1, dst 2 has no route
Rule 1, prefer d1, d2 is not routable
Rule 2, prefer d1, d2 dst scope does not match src scope
Rule 6, prefer d2, d2 precedence %d > d1 precedence %d
kvbuf_add_key: overflow when adding extra (%zu) and kl (%u)
new_requires_synthesis is NULL
Opening libnetwork.dylib
sockaddr is too big
not prefering 1, dst1 min rtt %f < dst2 min rtt %f, leeway %u small leeway %u
prefer 1, dst 1 is local, dst 2 is not
Rule 3a, prefer d2, d1 source is optimistic
Rule 8, prefer d2, d2 scope %d < d1 scope %d
dlopen(\"...libnetwork.dylib\") failed: %{public}s
%{public}s dst2 is NULL
si_destination_lookup for dst2 failed
Rule 7, prefer d1, d2 src is not native
fcntl(%d, F_GETFL, 0) failed: %m
prefering 2, dst1 min rtt %f > dst2 min rtt %f, leeway %u small leeway %u
prefer 2, dst 1 has no successful connections and %u attempts
ipv4_addr is NULL
prefer d1, known while d2 not known
prefer d2, known while d1 not known
Rule 5, prefer d2, d1 dst label does not match src label
prefer 1, dst 1 is loopback, dst 2 is not
fcntl(%d, F_SETFL, %d) failed: %m
xpc_user_sessions_get_foreground_uid() failed with error %d - %s
setsockopt(%d, SOL_SOCKET, SO_NOSIGPIPE, ...) failed: %m
not prefering 2, dst1 min rtt %f > dst2 min rtt %f, leeway %u small leeway %u
prefer 1, dst 2 has no successful connections and %u attempts
socket(PF_SYSTEM, SOCK_DGRAM, SYSPROTO_CONTROL) failed: %m
recv failed: %m
prefer 2, dst 2 is loopback, dst 1 is not
Rule 3a, prefer d1, d2 source is optimistic
Rule 9, prefer d2, d2 shares more common prefix
kvbuf_grow: overflow when adding kv->datalen (%u), delta (%u), and extra (%u)
nat64_v4_requires_synthesis(%{network:in_addr}d) == %{bool}d
prefer 2, dst 1 has no route
Rule 2, prefer d2, d1 dst scope does not match src scope
Rule 3, prefer d1, d2 source is deprecated
new_path_check is NULL
libnetwork.dylib did not set nat64_v4_requires_synthesis
libnetwork.dylib did not set nat64_v4_synthesize
ioctl(%d, CTLIOCGINFO, ...) failed: %m
setsockopt(%d, SOL_SOCKET, SO_RCVBUF, %d) failed: %m
Rule 7, prefer d2, d1 src is not native
Rule 8, prefer d1, d1 scope %d < d2 scope %d
Rule 9, prefer d1, d1 shares more common prefix
kvbuf_grow: overflow when rounding %u to nearest chunk size (%u)
nat64_v4_synthesize(%d, %{network:in_addr}d, ...) returned %d
kvbuf_append_kvbuf: overflow when subtracting sizeof(uint32_t) (%zu) from kv2->datalen (%u)
(dst_sa->sa_len %u > sizeof(cache_entry->dce_entry.d_dst.addr))
no preference, equal min rtt %f
prefer dst 2, dst 1 is p2p, dst 2 is not
Rule 1, prefer d2, d1 is not routable
Rule 5, prefer d1, d2 dst label does not match src label
Rule 6, prefer d1, d1 precedence %d > d2 precedence %d
_muser_call: Error from xpc pipe (%d), retrying
%{network:sockaddr}.*P@%u %c %{network:sockaddr}.*P@%u
prefer 2, dst 2 is local, dst 1 is not
new_synthesize is NULL
send failed: %m
```
