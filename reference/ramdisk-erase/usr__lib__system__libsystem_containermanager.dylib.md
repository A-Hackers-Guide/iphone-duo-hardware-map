# `/usr/lib/system/libsystem_containermanager.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 480,768 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 38 (Size: 3240)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (19)

- `/usr/lib/system/libsystem_containermanager.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libcopyfile.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libremovefile.dylib (compatibility version 1.0.0, current version 96.40.3)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_collections.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_darwin.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libsystem_featureflags.dylib (compatibility version 1.0.0, current version 111.0.0)`
- `/usr/lib/system/libsystem_info.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_notify.dylib (compatibility version 1.0.0, current version 368.40.2)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_sandbox.dylib (compatibility version 1.0.0, current version 3051.40.81)`
- `/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`

## Entitlements

```xml
  - no entitlements
```

## Strings (979)

```
PERSONA_VOLUME_NOT_MOUNTED
PERSONA_BUNDLE_LOOKUP_FAILED
container_paths_enumerate_containers_at_block_invoke
|
container_create_or_lookup_app_group_paths_for_platform
REPLACE_RECOVER
FAILED_MEMORY_ALLOCATION
*
container_notify_start
container_notify_increment_generation
CREATE_STAGING_DIRECTORY
INVALID_UNIQUE_PATH_COMPONENT
ReplyGroupIdentifiers
container_traverse_node_is_directory
CANNOT_OPERATE_ACROSS_MULTIPLE_USERS
upcall
B40@?0{container_pwd_s=II**}8^^{container_error_extended_s}32
container_delete
container_recreate_structure
MANAGED
ContainerMetadataSandboxToken
UNRECOGNIZED_MAGIC
FAILED_TO_CHECK_APP_GROUP_PROTECTION
container_bundle_copy_data_container
DestPath
container_copy_persona_unique_strings
FAILURE_TO_GET_ERROR_REPLY
ContainerMetadataTransient
SQLITE_UNEXPECTED_NUM_CHANGES
ReplySuccess
LNK
container_query_set_class
_container_query_reset_iterator
container_notify_set_queue
MISMATCHED_USER_REPLACE
USER_IDENTITY_DATA_INVALID
CORRUPT_METADATA
_container_init(): no container identifier available for process
startup
CONTAINER_SCHEMA_CREATE_FAILED
(%04u:0x%08llx:0x%08llx:0x%04lx:%02d:%04u:%04u:%04u:O%06o:%03d:%s%s%s:%s:%03d)[%s][%s]
_container_query_get_next_result_sync
Library/Caches
IDENTIFIER_NOT_FOUND_IN_DB
containers/Shared/SystemGroup
xpcService
CFFIXED_USER_HOME
container_query_operation_set_part
/private/var
container_query_operation_set_platform
container_query_operation_set_part_domain
Part
com.apple.containermanager.all-personas
Data
_container_init(): container path could not be set for process
[%s%s:%s:%u:%s:(%s%s%s):%s%s%s]%s
CACHE_INCONSISTENCY
INVALID_ENTITLEMENT_INFO
fs
ReplyDiskUsage
container_copy_code_signing_info_for_identifier
container_paths_copy_container_root_path_for_context
ReplyAuthorized
P.
ReplySandboxToken
containers/Bundle/Application
Containers/Data/TempDir
HOME
container_create_or_lookup_user_managed_assets_relative_path
ReplyRelativePath
NOT_ENTITLED_FOR_OPERATION
EXISTING_CONTAINER_CREATE
Containers/Data/InternalDaemon
B12@?0I8
unsupported rank_factor value
BAD_REPLY_CONTENTS
INVALID_DATA_SUBDIR
tempDir
container_references_set_uid
codesign
container_query_set_group_identifiers
container_notify_set_uid
container_repair_user_data
ContainerIdentifier
v12@?0i8
container_info_delete
_container_async_reclaim_disk_space_block_invoke_2
ContainerMetadataExisted
FAILED_TO_FETCH_PERSONA_INFO
com.apple.containermanagerd.system
kern.bootsessionuuid
repair
((void)\"container_bitvector_set(): index too large for array\", 0)
AMBIGUOUS_RESULT
WRONG_CONTAINER_PLATFORM
QUARANTINE_SUB_DIRECTORY_FAILED
appGroup
_container_query_operation_set_private_flags
 {NEW}
container_notify_set_class
FAILED_TO_READ_CODESIGN_INFO
EGID
PID
Explicit
B24@?0Q8^v16
container_bitvector.h
com.apple.containermanagerd.home-repair
FAILED_TO_CREATE_GLOBAL_DIRECTORY
ReplyFlags
container_notify_get_generation
((void)\"container_bitvector_set(): index too large for element width\", 0)
container_system_group_path_for_identifier
container_copy_info_value_for_key
((void)\"container_bitvector_get(): index too large for element width\", 0)
ReplyInfoValue
EXISTING_CONTAINER_REPLACE
container_traverse_node_get_optional_parent_fd
container_delete_array_of_containers
container_set_code_signing_info_for_identifier
%s/%s/%s
CreateIfNecessary
REPLACE_MOVE_TO_TEMP
LaunchPersona
IdentifiersArray
T
container_bundle_copy_data_container_path
RECURSIVE_CONFIG_FILE
CONTAINER_NOT_FOUND
NumRetryCrashes
SuccessorContainer
CONTAINER_REPLACE
container_traverse_node_get_optional_dp_class
Disabling
command
container_query_set_persona_unique_string
CREATE_TEMP_DIRECTORY
v48@?0I8Q12^v20I28Q32@?<v@?^vi^{container_error_extended_s=QQ*i*^{container_query_s}^{container_references_s}^{container_notify_s}}>40
container_entitlements_copy_container_identifiers
container_query_set_container_identifiers
upgrading
container_notify_set_event_handler
FAILED_TO_RECREATE_CONTAINER_DATA_SUBDIR
AMBIGUOUS_PERSONA
CodesignTeamIdentifier
container_query_set_instance_uuid
Library/Preferences
REMOVE_INDIVIDUAL_STAGING_DIRECTORY
container_create_or_lookup_app_group_path_by_app_group_identifier
DATA_PROTECTION_FAIL
Containers/Temp/Shared/AppGroup
containers/Temp/Shared/SystemGroup
container_notify_set_flags
INVALID_PARAMETERS
MCMMetadataUUID
containers/Bundle/Framework
G.
container_error_t container_regenerate_uuid(container_object_t _Nonnull)_block_invoke
ContainerUUID
INVALID_PERSONA
v28@?0^v8i16^{container_error_extended_s=QQ*i*^{container_query_s}^{container_references_s}^{container_notify_s}}20
C.
com.apple.security.application-groups
CREATE_BASE_DIRECTORY
containers/Data/ProtectedSystem
CACHE_FAILED_TO_REBUILD
container_create_or_lookup_path_for_platform
container_delete_all_container_content
Documents
<unknown>
pluginData
aclInfo
XPC_UNKNOWN_REPLY
container_traverse_node_get_optional_flags
ContainerMetadataOwnership
INVALID_QUERY_OBJECT
container_paths_context_set_class
/Data
container_query_operation_set_client
com.apple.containermanager.sandbox-extensions
container_info_put
container_delete_array_of_containers async obliteration
UNRECOGNIZED_VERSION
OnBehalfOfSelf
ReplyErrorExtended
GroupIdentifiers
ContainerMetadataInstanceUUID
UNDEFINED_CONTAINER_CLASS
MISMATCHED_CLASS_REPLACE
INVALID_OWNERSHIP
 true
container_query_set_include_other_owners
container_subdirectories_for_class
OwnershipMode
NOTIFY_GET_STATE_FAILED
container_operation_complete_background_tasks
com.apple.security.system-groups
NewContainer
%llu→(%llu) %s at path [%s] with errno (%d) %s; %s
SET_SANDBOX_MAPPING
EUID
personaUniqueString
%s/%s
/private/var/containers
<none: resuming>
IncludeUnowned
NOT_CODESIGNED
perUserApp
container_object_sandbox_extension_activate
computed index too large for minimal perfect hash
((void)\"container_bitvector_get(): index too large for array\", 0)
MCMMetadataContentClass
Containers/Data/Application
Containers/Data/XPCService
container_operation_delete_array
app
Unavailable
OwnerIdentifiersArray
container_get_info_value_for_key
containers/Temp/Bundle/PluginKitPlugin
container_operation_set_data_protection
vpnData
<multiple>
com.apple.containermanager.current-persona
file-read-data
PersonaKernelID
ContainerUID
REPLACE_REMOVE
container_traverse_node_get_optional_uid
paths
AppGroup
MCMMetadataIdentifier
ReplyOwnerIdentifiers
DIR
container_flush_persona_cache
container_debug_dump_state
container_query_iterate_results_with_subquery_sync
OptionsDictionary
container_query_create_from_container
CREATE_REPLACE_DIRECTORY
Containers/Temp/Data/XPCService
com.apple.containermanager connection release hysteresis
@(#)VERSION:Container Manager: Oct  3 2026 16:08:52; MobileContainerManager_system-833.40.18.0.1~68/arm64e
OwnershipGID
unknown
container_traverse_node_get_optional_gid
locking
telemetry
container_notify_has_changed
Command
RESTORE_CONTAINER
PERSONA_DID_NOT_PROPAGATE
Containers/Temp/Data/Application
CodeSigningInfo
container_query_operation_set_flags
CACHE_ADD
container_test_set_locks_and_restart
yes
com.apple.containermanagerd.user-invalidated
DEFAULT
ContainerMetadataPath
NOT_ENTITLED_FOR_APP_GROUPS
Containers/Temp/Data/PluginKitPlugin
appData
UUID
ContainerPersonaUniqueString
ErrorPath
SANDBOX_CONSUME_TOKEN_ERROR
CLIENT_NOT_SANDBOXED
com.apple.containermanagerd
container_object_free
Transient
ContainerMetadataCreator
REGENERATE_UUID_MOVE
STAGE_SHARED_CONTENT_FAILURE
v16@?0Q8
containers/Temp/Bundle/Application
systemData
container_traverse_node_get_optional_file_id
REPLACE_URL
BASE_PATH_MISMATCH_FOR_PERSONA
com.apple.security.system-container
SYSTEM_PROXY
REMOVE_STAGING_DIRECTORY
WRONG_AGENT
INVALID_IDENTIFIER
USER_NOT_FOUND
container_references_iterate_by_owner_sync
INVALID_URL
USER_HAS_NO_HOME_DIRECTORY
END_OF_RESULT_SET
INVALID_CONFIG_FILE
Entitlements
container_references_iterate_by_group_sync
container_create_or_lookup_for_platform
ReplyPath
BAD_INITIALIZER_VALUES
SANDBOX_RELEASE_HANDLE_ERROR
containers/Data/System
%llu→(%llu) %s; %s
ACL_FAILURE
Containers/Temp/Data/InternalDaemon
unspecified
disk
container_get_info
Value
FAILED_TO_FETCH_CLIENT_LAUNCH_PERSONA
Enabling
metadata
container_copy_path
temp-
FAILED_TO_DELETE_OPERATION_PLIST
Containers/Temp/Data/VPNPlugin
sandbox
ReplyContainerSet
BUNDLE_ID_UNSAFE_FOR_FILESYSTEM
CONTAINER_SCHEMA_UPDATE_FAILED
_container_init(): system session processes cannot be containerized
XPC_SETUP
EXCEPTION
posixUID
AuditToken
DATA_SMALLER_THAN_HEADER
INVALID_UUID
READ_DELETE_MANIFEST_DIRECTORY
container_paths_enumerate_containers_at
container_references_operation_set_flags
com.apple.security.system-group-containers
RESTORE_PATH_EXISTS
INVALID_COMMAND
XPC_INTERRUPTED_REPLY
SQLITE
INVALID_BUNDLE_PATH
ReplyPersonaUniqueStringsArray
ZERO_DELETE_MANIFEST
INVALID_UID
MISSING_ELEMENTS
container_get_instance_uuid
Container
ContainersArray
consuming
BundlePath
SANDBOX_EXTENSION_NOT_FOUND
STALE_XATTR
longterm
container_notify_post
SandboxToken
ReplyExisted
CREATE_CONTAINER_CLASS_DIRECTORY
SANDBOX_TOKEN_UNAVAILABLE
DURING_STARTUP
container_paths_context_set_uid
container_operation_delete
container_traverse_node_optional_has_acl
container_notify_set_generation
index of string could not be looked up
WRITE_ENTITLEMENT_FILE
PENDING_UPDATE_NO_LONGER_VALID
FAILED_TO_FETCH_VOUCHER_PROXIMATE_PERSONA
container_set_test_lock
container_get_posix_ownership
<NULL>
:
INVALID_CONTAINER_OBJECT
container_query_set_uid
COMMAND_QUEUE_EXHAUSTED
MobileContainerManager
WARNING
WRITE_DATA_PROTECTION_OPERATION
WRITE_MIGRATION_STATUS
LIBRARY_DIRECTORY_CREATE_FAILED
com.apple.private.security.restricted-application-groups
XPC_TERMINATION_IMMINENT
INVALID_SANDBOX_EXTENSION_TYPE
Expected a mode_string of size CONTAINER_MODE_STRING_SIZE
containers/Temp/Bundle/Framework
container_traverse_node_get_name
container_create_or_lookup_system_group_paths
ErrorMessage
FAILED_TO_ISSUE_SANDBOX_EXTENSION
container_debug_copy_state
ReplyContainerInfos
all vertices of the edge have been visited
container_process_restored_container
FAILED_TO_FETCH_PENDING_UPDATES
container_traverse_node_is_symlink
Library
SystemData
OwnershipUID
STARTUP_INVALID_COMMAND_LINE_OPTION
Enable
MCMMetadataUserIdentity
containers/Bundle/VPNPlugin
/tmp/
lifecycle
com.apple.containermanager.primary-persona
SYSTEM
CACHE_REMOVE
systemGroup
TMPDIR
REG
VALUE_NOT_FOUND_FOR_KEY
ReplyContainersArray
ReplyFacts
query
container_query_set_identifiers
D.
Ownership
Key
B24@?0r*8^v16
((void)\"container_bitvector_set(): bad argument\", 0)
container_group_container_identifiers_for_current_user
ContainerClass
USER_HOME_DIRECTORY_MISSING
protectedSystem
container_flush_container_cache
container_paths_context_set_flags
containers/Bundle/PluginKitPlugin
Containers/Bundle/Application
 invalidation
Identifier
REMOVE_LEGACY_DIRECTORY
WRITE_METADATA_DICTIONARY
UNSUPPORTED
INVALID_FILE_MODE
TestLock
%s
SourcePath
READ_ENTITLEMENT_FILE
container_query_iterate_results_with_identifier_sync
CmCo:3:%llu:%u:%s:%s:%s:%s:%s:%u:%u:%s:%s
container_operation_delete_reclaim_disk_space
container_traverse_directory
container_traverse_node_get_subordinate_count
container_delete_user_managed_assets
SAME_CONTAINER_REPLACE
PATH_NOT_FOUND
Containers/Temp/Data/TempDir
FD
_container_query_set_internal_uuid
false
container_delete_all_data_container_content_for_current_user
INVALID_METADATA
GET_METADATA
USER_HOME_DIRECTORY_INACCESSIBLE
~
vpn
daemon
container_traverse_node_get_optional_link_count
codesignmapping
success
ACTION_NOT_PERMITTED_BY_CLIENT_UID
INVALID_FILE_ACTION
Containers/Temp/Bundle/Application
B32@?0*8Q16^^{container_error_extended_s}24
container_delete_with_class_and_identifier_for_current_user
container_create_or_lookup_user_managed_assets_path
Path
container_error_free
THREAD_STORAGE_EXHAUSTED
container_paths_copy_container_from_path
container_references_set_persona_unique_string
container_bitvector_set
GENERAL_FILESYSTEM_ERROR
B20@?0I8r*12
NIL_IDENTIFIER
CREATE_DEATH_ROW_DIRECTORY
DATA_PROTECTION_FAIL_LOCKED
Containers/Data/VPNPlugin
v16@?0^v8
container_copy_info
INVALID_REPLY
FAILED_TO_REGISTER_PROTECTED_APP_GROUP
B64@?0{container_paths_definition_s=QQS(container_paths_definition_owner_u=Q{?=QII}{?=Q*})*B}8
_container_authorize_execute
com.apple.private.security.daemon-container
container_system_path_for_identifier
CANNOT_SET_QUERY_PARAMETERS_AFTER_EXECUTE
container_operation_copy_superseded_block_invoke
i24@?0r^v8r^v16
container_perform_data_migration_for_current_user
NOT_SECURED_BY_PLATFORM_POLICY
IDENTITY_ALREADY_SUPERSEDED
ReplyWarnings
container_query_iterate_results_sync
ReplyContainerTokens
PrivateFlags
tmp
IsRelative
ContainerMetadataUMARelativePath
INVALID_METADATA_URL_MISMATCH
INVALID_EXECUTABLE_PATH
ATTEMPT_TO_MUTATE_AFTER_EXEC
container_create_or_lookup_app_group_paths_from_entitlements_4ls
container_acquire_sandbox_extension
READ_METADATA
NO
container_get_all_with_class_for_current_user
FAILED_TO_BACKUP_FILE_DURING_SCHEMA_UPDATE
BUNDLE_OWNER_MIGRATION_FAIL
%s/%s.plist
ReplyPayload
container_query_copy
ReplyInfoDictionary
container_invalidate_code_signing_cache
ErrorPOSIXErrno
container_query_set_ownership
CACHE_INVALID_DATA
NOTIFY_REGISTER_FAILED
ProxyForClient
container_traverse_node_get_optional_mode
container_info_modify
((void)\"container_bitvector_get(): bad argument\", 0)
ContainerMetadata
XPC_INVALID_REPLY
container_references_set_persona_unique_string_block_invoke
WRITE_REPLACE_OPERATION
container_traverse_node_is_regular_file
container_replace
STAGE_FOR_DELETE
CmCo
container_operation_copy_superseded
cache
schema
persona
ReplyGeneration
PersonaData
container_paths_context_set_persona_unique_string
containers/Temp/Data/ProtectedSystem
Logs
container_traverse_node_get_path
container_perform_data_migration
ReplyCacheable
SETUP_PROXY
CONTAINERS_WITH_CLASS_INIT
PART_SUBDIR_CREATION_FAILED
NO_PATH_ONLY
container_references_set_class
com.apple.containermanager
container_bitvector_get
Flags
REMOVE_TEMP_CONTAINER
INVALID_CODE_SIGNATURE
Containers/Shared/AppGroup
containers/Temp/Data/System
ContainerMetadataInfo
DESTROY_CONTAINER
UNKNOWN
containers/Temp/Bundle/VPNPlugin
mobile
container_user_managed_assets_relative_path
UNABLE_TO_GET_USER_DETAILS
INVALID_AUDIT_TOKEN
_container_query_get_result_at_index
true
PersonaUniqueString
INVALID_FLAGS
container_paths_context_set_transient
asprintf failed
plugin
container_traverse_node_get_optional_alloc_size
v16@?0r*8
container_disk_usage
MCMMetadataInfo
Containers/Data/PluginKitPlugin
container_references_add
Platform
ErrorType
UNKNOWN_SUBDIRECTORIES_FOR_CLASS
.com.apple.mobile_container_manager.metadata.plist
_container_init(): did not get a reply message back from xpc_pipe_routine
itemNameInfo
test
com.apple.containermanager.%s%s
v8@?0
container_query_set_transient
INSTANCE_UUID_MISMATCH
YES
no
SPURIOUS_NUL
container_operation_set_data_protection_block_invoke
container_traverse_node_get_depth_from_origin
issue in rank table calculation
NOPERSONA
UID
{%u:%u:%s}
container_user_managed_assets_path
container_query_count_results
VOUCHER_PROXIMATE_POINTS_TO_SELF
framework
database
computed index too large
FAILED_TO_PARSE_DELETE_MANIFEST
MCMMetadataInstanceUUID
OldContainer
ExecutablePath
MOVE_STAGING_TO_LIVE
INVALID_CLIENT_OBJECT
NOT_CONTAINERIZED
PATH_IS_INCOMPLETE_CONTAINER
INVALID_POSIX_PERMISSIONS_PLIST
InstanceUUID
container_set_info_value
STATE_RESET_RETRY_REQUEST
SystemDataDomain
B16@?0^{container_object_s=}8
ContainerUniquePathComponent
STALE_FS_NODE
CodesignIdentifier
DataProtectionClass
container_references_remove
container_regenerate_uuid
container_stage_shared_system_content
QUERY_NOT_EXECUTED
CONTAINER_IDENTITY_DATA_INVALID
xpc
notify
FAILED_TO_CHECK_CONTAINER_DATA_SUBDIR
 interrupted
MOVE_TO_DEATH_ROW
FAILED_TO_WRITE_DELETE_MANIFEST
MCMMetadataPersona
ERROR
container_notify_register_generation_handler
ErrorCategory
CREATE_SUB_DIRECTORY
container_class parameter is an invalid value (%llu > %llu < %llu)
Malformed attrlist on entry in [%s]; [entryCount] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(entryCount) = %zu
%{public}s: client persona did not propagate to container manager
Notify check failed, assuming that there are changes. THIS CAUSES A PERFORMANCE PENALTY.
container_copy_object
%{public}s(container, %{public}s)
container_delete_user_managed_assets
container_copy_info
WARNING: Calling %s with a notify object that has a previous error: %s
Update info; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, message = %s
container_delete_all_data_container_content_for_current_user
container_acquire_sandbox_extension
Failed to get container root path.
[%s] does not exist, assuming no containers.
%s: SPI MISUSE: persona_unique_string parameter is NULL
XPC connection to containermanagerd invalidated. Retry attempt %u of %u
_container_init(): sandbox_container_path_for_pid() failed: %d
getattrlistbulk failed on entry %u in [%s]; error = %{darwin.errno}d
sandbox_extension_issue_file failed for class %{public}s at path [%s]: %d
Registered for generation check; event = [%s], container_class = %llu
%s: SPI MISUSE: context cannot be NULL
Malformed attrlist on entry in [%s]; [aclInfo] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(aclInfo) = %zu
Query result; index [%zu] %s %s
Failed to register for generation event; event = [%s], container_class = %llu, status = %u
container_group_container_identifiers_for_current_user
container_recreate_structure
container_user_managed_assets_path
Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], bundle = [🔒%{private}s], root = [🔒%{private}s], executable = [🔒%{private}s], flags =
container_operation_delete_reclaim_disk_space
Unable to fetch platform from client for pid [%d]: %{darwin.errno}d
%s: SPI MISUSE: owner_identifiers is not an array or string
containermanagerd state reset, retry requested. Retry attempt %u of %u
%s: SPI MISUSE: node parameter is NULL
%s: SPI MISUSE: info_dict parameter is expected to be a dictionary
container_info_delete
container_delete_array_of_containers
Internal error: totalProcessedEntryCount (%u) was less than reprocessCount (%u)
%s: SPI MISUSE: identifiers is not an array or string
Posted event; event = %llu, event_name = [%s], container_class = %llu
%s: SPI MISUSE: context parameter is NULL
Query; euid = %u, uid = %u, class = %llu, identifier = [%s](%zu), flags = %llx
Failed to locate last path element in [%s]
%s: SPI MISUSE: domain parameter is NULL
Could not get entitlements for client
connection <%p/%llu/%llu; %p> invalidated
Query; euid = %u, uid = %u, class = %llu%s, identifier = [%s](%zu), gidentifier = [%s](%zu), instance = 🔒%{private}s, uuid = 🔒%{private}s, flags = %llx
Consumed sandbox extension; path = [%s], handle = %lld
Checked generation event; token = %d, container_class = %llu, check = %d
container_delete_with_class_and_identifier_for_current_user
container_subdirectories_for_class
Could not decode message into error: %{public}s
Malformed attrlist on entry in [%s]; [uid] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(uid) = %zu
XPC message proximate pid matches our pid; this is unexpected; our pid = %d, proximate pid = %d
Unable to get bundle root path from bundle at [🔒%{private}s]: %{public}d
Requesting multiple containers; class = %llu, temp = %d, euid = %u, uid = %u
Retrieving the path from a container which was fetched by a query without the CONTAINER_QUERY_FLAGS_RESULT_INCLUDE_PATH option. If you want the path from queried containers, set that option on the query. That will be much faster than what i
received superfluous connection%{public}s event, ignoring
Could not decode message into persona: %{public}s
Missing platform when trying to initialize a client object.
Client xpc object cannot set entitlements.
%s: SPI MISUSE: A query must not contain a persona for container_authorize*
Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, query = %s
Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu, identifier = [%s](%zu), flags = %llx
XPC connection to containermanagerd interrupted. Retry attempt %u of %u
Failed to post generation change; class = %llu, generation = %llu
container_info_modify
container_copy_code_signing_info_for_identifier
An empty string is not a valid group container identifier.
NULL client when fetching launch persona
%s: SPI MISUSE: Unknown container class
Unable to fetch executable path from client for pid [%d]: %{darwin.errno}d
Malformed attrlist on entry in [%s]; aclInfo magic mismatch; expected = 0x%x, got = 0x%x
container_invalidate_code_signing_cache
Failed stat container root [%{private}s]: %{darwin.errno}d
Set data protection; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, dpclass = %d, container = 🔒%{private}s, flags = %llx
No usable container in reply during %s
References query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, query = %s
%s: SPI MISUSE: Provided container class is not a valid container class: %llu
Registered generation dispatch handler; token = %d, container_class = %llu
getpwnam_r(%s) returned %{public, darwin.errno}d
container_create_or_lookup_path_for_platform
WARNING: Calling %s with a references that has a previous error: %s
%{public}s: client had ambiguous persona during request
container_system_group_path_for_identifier
container_flush_container_cache
container_flush_persona_cache
container_perform_with_client_context
Client xpc object has a malformed audit token.
NULL client when fetching test mode
%s: SPI MISUSE: path parameter is NULL
Malformed attrlist on entry in [%s]; [allocSize] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(allocSize) = %zu
sysconf(_SC_GETPW_R_SIZE_MAX) <= 0: %{public}ld
container_set_info_value
container_process_restored_container
Could not allocate memory to initialize a client object.
Failed to find a candidate buffer to scavenge!
container_create_or_lookup_app_group_paths_for_platform
NULL client when fetching entitlements
Malformed attrlist on entry in [%s]; [mode] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(mode) = %zu
skipping mount point or trigger at [%s]/[%s]
Client xpc object is not a dictionary.
Failed to read metadata plist [%{private}s]: %{darwin.errno}d
%{public}s: enumeration of path [%s]: success = %d, found container = %d
Calling out to client; token = %d, event = %llu, container_class = %llu
container_bundle_copy_data_container
Failed to determine if %{private}s exists: %{darwin.errno}d
%{public}s: success
%s: SPI MISUSE: notify parameters cannot be changed after container_notify_start() or container_notify_has_changed()
Malformed attrlist on entry in [%s]; %s.attr_length too small; expected >= %lu, got = %u
%s: SPI MISUSE: container parameter is required
NULL client when fetching platform
NULL client when copying
%{public}s(container, %{public}s): no sandbox token in container
%s: SPI MISUSE: notify parameter is NULL
container_create_or_lookup_app_group_path_by_app_group_identifier
container_retry_test
%{public}s: enumeration failure opening container dir [%llu]: %s
container_operation_set_data_protection
Insufficient room (%zu bytes) to read length of entry %hu in [%s]; need %zu
%s: SPI MISUSE: out_generation parameter is NULL
Posted generation change event; event_name = [%s], container_class = %llu
%s: SPI MISUSE: keys_array parameter is required
Metadata plist [%{private}s] is has a corrupt UUID [%{public}s].
Malformed attrlist on entry in [%s]; [fileID] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(fileID) = %zu
container_copy_path
Could not get code sign identifier from audit token to initialize a client object for pid [%d].
%s: SPI MISUSE: enumerator cannot be NULL
Failed to locate an attr buf
Canceled registered event; token = %d, container_class = %llu
%s: SPI MISUSE: persona_unique_string is NULL but is required for data separated mount point
Unable to obtain a task name port right for pid %i: %{public}s (0x%x)
_container_init(): sandbox_get_container_expected() failed: %d
Overflowed link count [%u]
container_regenerate_uuid
container_set_data_protection_for_current_user
connection <%p/%llu/%llu> shared; cnt = %lld
Could not get code sign status from audit token for pid [%d] identifier [%s]: %{darwin.errno}d
NULL client when fetching euid
container_debug_copy_state
WARNING: Calling %s with a query that has a previous error: %s
connection <%p/%llu/%llu> released (shared; handler); cnt = %lld
Metadata plist [%{private}s] has a corrupt instance UUID [🔒%{private}s].
Wait for background task completion; disposition = 0x%x
Unable to fetch persona from persona id [%u]
Requesting disk usage; class = %llu, identifier = %{private}s
container_operation_delete
container_operation_complete_background_tasks
%s: SPI MISUSE: group_identifiers is not an array or string
container_user_managed_assets_relative_path
container_paths_context_t
%s: SPI MISUSE: Cannot use CONTAINER_PATHS_PREFIX_TYPE_USER_HOME with global container class %llu
%s: SPI MISUSE: container required but NULL
container_operation_copy_superseded
connection <%p/%llu/%llu; %p> canceled after timeout; cnt = %lld
Requesting container lookup; class = %llu, identifier = %{private}s, group_identifier = %{private}s, create = %d, temp = %d, euid = %u, uid = %u
Failed to fetch our own audit token
connection <%p/%llu/%llu> created; cnt = %lld
container_references_t
container_query_t
%s: SPI MISUSE: identifiers parameter is NULL
container_sandbox_extension_revoke(): error %d releasing sandbox extension
container_info_put
getpwnam_r(%s): user not found
container_replace
container_delete
Requesting app group container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], identifier = %{private}s, euid = %u, uid = %u, platform = %u
%s: SPI MISUSE: Attempt to free container_error_extended_t that is owned by a container_query_t. Ignoring.
Malformed attrlist on entry in [%s]; [linkCount] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(linkCount) = %zu
container_stage_shared_system_content
container_copy_sandbox_token
container_sandbox_extension_consume(): error %d consuming sandbox extension
container_create_or_lookup_user_managed_assets_relative_path
Missing a codesign identifier when trying to initialize a client object.
NULL client when fetching pid
Attempted to iterate directories starting at a path that was too long: [%s]
Malformed attrlist on entry in [%s]; length field too large; start = %p, length = %u, sizeof(length) = %zu
%s: SPI MISUSE: unsupported mode bits, only access perm bits are supported
Failed to register generation dispatch handler; container_class = %llu, status = %u
Got generation state; token = %d, container_class = %llu, generation = %llu
container_create_or_lookup_path_for_current_user
Malformed attrlist on entry in [%s]; [mountStatus] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(mountStatus) = %zu
%s: SPI MISUSE: invalid container part: %llu
Replacing existing notify handler; class = %llu, event = %llu
Failed to check generation state; container_class = %llu, status = %u
realpath_np([%{private}s]) failed: %{public, darwin.errno}d
container_create_or_lookup_app_group_paths_for_current_user
container_delete_all_container_content
container_set_code_signing_info_for_identifier
NULL client when fetching code sign team identifier
NULL client when fetching signed
Client passed NULL path_to_bundle parameter.
No client object to encode.
_container_init(): could not create xpc_pipe: %d
%s: SPI MISUSE: Attempt to free container_object_t that is owned by a container_query_t. Ignoring.
Failed to set generation state; container_class = %llu, generation = %llu, status = %u
Failed to post generation changed event; container_class = %llu, generation = %llu, status = %u
NULL client when fetching egid
Metadata plist [%{private}s] is missing an identifier.
Malformed attrlist on entry in [%s]; [returned] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(returned) = %zu
%s: SPI MISUSE: info_dict parameter is required
Failed to issue sandbox extension to [🔒%{private}s] for containermanagerd
Unable to obtain a task info for pid %i: %{public}s (0x%x)
Malformed attrlist on entry in [%s]; length field exceeds reported buffer length; start = %p, length = %u, sizeof(length) = %zu
Malformed attrlist on entry in [%s]; [type] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(type) = %zu
%{public}s: error = ((container_error_t)%{public}llu) %{public}s
%s: SPI MISUSE: invalid container class
%s: SPI MISUSE: node_handler parameter is NULL
Failed to get state in generation dispatch handler; token = %d, status = %u
kpersona_getpath(%u) returned %{public, darwin.errno}d
container_create_or_lookup_for_current_user
%s: SPI MISUSE: Invalid flags specified: 0x%08llx
Read entry length %u for entry %hu but that put us off the end of the buffer
%s: SPI MISUSE: container_class parameter is an invalid value (%llu > %llu < %llu)
Failed to post notification; class = %llu, event = %llu, name = [%s]
Fetched persona for pid; pid = %d, persona = %u
%{public}s: error = %{public}s
Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu%s, identifier = [%s](%zu), gidentifier = [%s](%zu), persona = 🔒%{private
%s: SPI MISUSE: handler block cannot be NULL
Skipping update of [%s] from [%s] since UUIDs don't match.
Enumerate; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, context<path = [%s], class = %llu, flags = 0x%llx, persona = [%{public}s], uid = 
NULL client when fetching persona unique string
Malformed attrlist on entry in [%s]; [flags] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(flags) = %zu
Malformed attrlist on entry in [%s]; %s.attr_length is zero
%{public}s: client is not entitled
getpwuid_r(%{public}u) returned %{public, darwin.errno}d
Requesting multiple containers; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], class = %llu, temp = %d, euid = %u, uid = %u
Query; euid = %u, uid = %u, query = %s
Could not append element [%s] of length %zu to path [%s] because it would make the path longer than MAXPATHLEN
%{public}s connection sharing
%s: SPI MISUSE: query parameter is NULL
container_set_test_lock
Failed to create pthread key. container_perform_with_client_context() cannot continue; errno = %{darwin.errno}d
_container_init(): unexpected error type: %llu
Malformed attrlist on entry in [%s]; [gid] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(gid) = %zu
Failed to cancel generation dispatch handler; token = %d, status = %u
Registered for event; token = %d, event = %llu, name = [%s], container_class = %llu
container_get_all_with_class_for_current_user
Unable to get executable path from bundle at [🔒%{private}s]: %{public}d
connection <%p/%llu/%llu> freed; cnt = %lld
Failed to open [%s]; error = %{darwin.errno}d
Malformed attrlist on entry in [%s]; [error] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(error) = %zu
Failed to convert uid to uuid for required instance uuid; uid = %u, errno = %{darwin.errno}d
NULL client when fetching signature valid
No client xpc object to decode.
Failed to find managed personas; error = %{darwin.errno}d
Failed to fetch path for persona; persona_id = %u, error = %{darwin.errno}d
%{public}s: client uid is not permitted, uid = %{public}u
%s: SPI MISUSE: container parameter is NULL
Update info; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu, identifier = %s, key = [%s](%zu), flags = %llx
NULL client when fetching code sign identifier
connection <%p/%llu/%llu> will be canceled in %lld seconds; cnt = %lld
Insufficient room (%zu bytes) to read length of skip entry %hu in [%s]; need %zu
No event handlers assigned; container_class = %llu
Failed to register one or more event handlers; container_class = %llu, expected = %zu, registered = %zu
Set state; token = %d, generation = %llu, container_class = %llu
%s: SPI MISUSE: keys_array parameter is expected to be an array of strings
container_disk_usage
failed to generate connection for sharing of type %llu, purpose %llu: %llu
Unable to get foreground uid for default ownership; error = %{darwin.errno}d
Replacing existing notify queue; class = %llu
%s: SPI MISUSE: event parameter is invalid (%llu/%llu)
A NULL string is not a valid group container identifier.
Failed to issue sandbox extension to [%{private}s] for containermanagerd
Unable to get bundle from [🔒%{private}s]
Could not decode message into container object: 🔒%{private}s
%s: SPI MISUSE: Attempt to free container_error_extended_t that is owned by a container_references_t. Ignoring.
Could not get platform from audit token to initialize a client object for pid [%d].
%s: SPI MISUSE: Cannot use CONTAINER_PATHS_PREFIX_TYPE_DATA_VOLUME_MOUNT_POINT with edu mode user %u
Malformed attrlist on entry in [%s]; [dataProtectionClass] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(dataProtectionClass) = %zu
Generation dispatch handler fired; token = %d, generation = %llu, container_class = %llu
container_copy_persona_unique_strings
Enumerate
container_operation_delete_array
%s: SPI MISUSE: successor provided but not valid
%s: SPI MISUSE: references parameter is NULL
%s: SPI MISUSE: fd argument is required
Revoked sandbox extension; handle = %lld
container_create_or_lookup_path
Client xpc object has a malformed entitlements.
NULL client when fetching is alive
%s: SPI MISUSE: entitlement_read_handler block is required
_container_init(): got error back from xpc_pipe_routine: %d
Malformed attrlist on entry in [%s]; [itemNameInfo] field exceeds reported buffer length; start = %p, end = 0x%lx, sizeof(itemNameInfo) = %zu
container_notify_t
Failed to get generation state; container_class = %llu, status = %u
Unable to get user (%u) home path, container results may not be reliable; error = %{public}s
%s: SPI MISUSE: Attempt to free container_error_extended_t that is owned by a container_notify_t. Ignoring.
NULL client when fetching platform binary
Unable to get user home path, container results may not be reliable; error = %{public}s
Container delete; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, manifest = %{private}s
Malformed attrlist on entry in [%s]; length (%u) exceeds remaining buffer (%zu); buffer = %p, buffer_end = %p
got error while processing entry %hu in [%s]; error = %{darwin.errno}d
container_perform_data_migration_for_current_user
container_create_or_lookup_user_managed_assets_path
Unable to obtain persona info for pid %i: %{public, darwin.errno}d
connection <%p/%llu/%llu> released (shared; canceler); cnt = %lld
Empty payload from state dump
Malformed attrlist on entry in [%s]; [%s][attr_dataoffset] field exceeds reported buffer length; start = %p, end = 0x%lx, attr_dataoffset + attr_length = %zu
container_copy_from_path
 class=%{public, signpost.description:attribute}llu 
%{public}s: enumeration failure processing container [%s][%llu]: %s
connection <%p/%llu/%llu> released; cnt = %lld
Undefined disposition value.
XPC message has no proximate persona
%{public}s: client sent invalid parameters
%s: container_query_set_class() is required
%s: SPI MISUSE: container class is not set or is invalid (%llu)
Metadata plist [%{private}s] is missing a UUID.
%s: SPI MISUSE: container_query_set_class() is required
voucher proximate; pid = %d, persona = %u, fetched = %s
%{public}s(container, %{public}s): %{public}s container extension
container_system_path_for_identifier
Replace; old = %s, new = %s
container_copy_info_value_for_key
Updated container during %s: %s
Evaluating persona; persona_id = %u, path = [%s]
Disposition unsupported.
container_debug_dump_state
Could not register for user invalidated notifications; status = %u
container_sandbox_extension_revoke_all(): error %d releasing sandbox extension
Failed to register for event; event = [%s], container_class = %llu, status = %u
getpwuid_r(%{public}u): user not found
container_create_or_lookup_system_group_paths
NULL client when fetching uid
%{public}s: failed (errors during enumeration)
Failed to allocate a continuation!
Entry %hu in %s did not include name information even though we requested it.
Unable to get mobile uid for default ownership; error = %{darwin.errno}d
%s: SPI MISUSE: key parameter is NULL
Updated container during replace: %s
container_repair_user_data
Could not decode message into container object: NULL
Failed to allocate an attribute buffer!
fgetattrlist for [%s] failed; error = %{darwin.errno}d
Could not allocate memory to merge container arrays: %zu + %zu
container_bundle_copy_data_container_path
Could not allocate memory to initialize a client object for pid [%d].
NULL client when fetching sandbox state
Wait for obliteration; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u
References query; euid = %u, uid = %u, query = %s
%s: SPI MISUSE: query has already been executed
Retrieving the info from a container which was fetched by a query without the CONTAINER_QUERY_FLAGS_RESULT_INCLUDE_INFO option. If you want the info from queried containers, set that option on the query. That will be much faster than what i
%s: SPI MISUSE: generation parameter is invalid
container_create_or_lookup_for_platform
NULL client when fetching audit token
%s: SPI MISUSE: prefix parameter is NULL
Supersede container; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, successor = 🔒%{private}s, predecessor = 🔒%{private}s, flags = %llx
Failed to create a continuation
container_create_or_lookup_app_group_paths_from_entitlements
Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], class = %llu, identifier = %{private}s, group_identifier = %{private}s, create = %d,
%s: SPI MISUSE: predecessor required but not valid
Malformed attrlist on entry in [%s]; [%s][attr_dataoffset] field is negative; start = %p, end = 0x%lx, attr_dataoffset = %d, attr_length = %u
%{public}s: client had incorrect persona during request
Query result; index [%u] %s
```
