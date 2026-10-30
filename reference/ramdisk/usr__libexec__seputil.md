# `/usr/libexec/seputil`

From the upgrade restore ramdisk (141-29011-104.dmg). 204,320 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2312)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, PIE
```

## Linked libraries (6)

- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.applesepmanager.allow</key>
	<true/>
	<key>com.apple.private.kernel.get-kext-info</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleSEPUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (754)

```
Kernel message log has %llu entries\n
test_case
%s: can't read in scrt\n
Sources/AppleSEPManager
i24@?0^{?=Q{?=*Q}}8^B16
Failed to get debug variable\n
Cannot merge statistics with mismatching classes
Issue cannot have a time of less than or equal to 0
aggregate->_reason
Cannot merge issues with different classes
preflight: FAIL: could not parse img4
get-nonce
\t\t--securitymode           Request SEP effective production status and security mode\n
%s: No SEP present on this device\n
%s: ERROR: %d\n
%s: can't read in infile\n
Cannot merge statistics with mismatching names
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/info_pair.c
\t\t--tunable-check <value>  Enable or disable tunable check mode.\n
%s: Missing debug var new value \n
%s: Provisional AP command failed\n
has-art
%s: inconsistent mailbox Log size : %d\n
%s: xART OS UUID setup failed: %d\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_statistic_bucket.c
Error seen...%s - %s\n
hilo-load-lth-transfer-message
has_system_token
 -instr-profile=
Failed to write output data file\n
\t\t--art-set <value>        Persist the supplied ART value to storage\n
%s: Couldn't populate gain test LTH: %d\n
realloc failed in fd_to_buf for size %zu\n
results->_statistics
%s: Purge system token failed\n
IODeviceTree:/arm-io/sep/iop-sep-nub/Sandcat
%s: Get mailbox log failed : %d\n
%s: Security mode command error: %x\n
Didn't find snid in patches IM4R, using default slot %u\n
img4: couldn't get bool property - fatal
lcrt_verify
%s: could not allocate buffer for scrt
Hilo update timer failed: 0x%x
%s: Failed to connect to sep\n
%s: mailbox raw log print failed\n
%s: prop %s val 0x%x\n
defaultInit
Created '%c%c%c%c' of size %u\n
\t\t--set-provisional <value> \tSet the provisional state of AP slot to 1 (provisional) or 0 (not provisional). Requires slot to be passed with --slot.\n
\t\t--requestpanic           Force a SEP/OS client requested panic\n
%s: Hilo accumulate test pattern failed: 0x%x\n
%s: Hilo get LTH failed: 0x%x\n
AppleSEPManager
%s: can't write out_buffer (to outfile)\n
results->_info
Unit test results only accept pass fail test cases
hilo-test-lth-transfer-attestation
%s: could not get master port\n
%s: lynx get chip serial number returned 0x%x\n
%s: couldn't write out LTH transfer message\n
Had to drop an issue (%d)
restore
rom
%s: Hilo load LTH transfer message failed: 0x%x\n
/usr/bin/llvm-cov
%s: Missing sub-command\n
w
was not 
IODeviceTree:/arm-io/sep/iop-sep-nub
Metric name cannot be null
restore+art
lynx_get_pub_key
\tART commands\n
art
requestpanic
\t\t--minblocks <value>      Optional argument to compare \"--art ctrtest\" good pages against\n
%s: failed to notify SEP/OS about erase install\n
v16@?0^{_xpc_activity_s=}8
Impossible results class %d\n
%s %s/%s\n
issue->_group
help
test-timeout
\t\t--launch-macos-app <ver> Launch MacOS serving app variant for the specified 16-bit hex version\n
%s: ERROR: At least one option required\n
%s: Missing output file\n
:
%s: lynx get app hash returned 0x%x\n
Skipping 
img4: failed to parse ART
\t\t--dump-cov <app>      Dump and reset coverage counters to object\n
%s: img4 dump failed\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/filesystem.c
results
Issue must have a group
show-epochs
hilo-load-lth
\t\t--test-timeout <value>   Set the default delay in milliseconds to wait for test completion (default=120000)\n
%s: Missing test input file\n
SEP status 0x%llx\n
%s: Data out size missing/out of range\n
%s: couldn't write out attestation\n
IOKit returned %x for kSEP_RunHandle\n
\t\t--l4panic                Force an L4 panic\n
%s: Incorrect value size for sepfw-loaded property\n
 for more detail
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/results.c
dump-cov
\t\tExamples:\n
%s: ping failed\n
%s: security mode query failed\n
%s: ttyin ' ' failed\n
%s: can't open '%s' for writing\n
Counter self-test result: %u/%u good\n
%s: No display params when expected!\n
raw ART: 
test-all
should-be-system-token
\tFirmware commands\n
\tExample: %s --wait --load /path/to/foo\n
%s: read firmware failed\n
ART cleared from storage
ERR: could not get the machine's unique identifier, reason: %s\n
hilo-check-gain-test-lth
%s: minblocks out of range\n
 because coverage was 0%
Unit test results cannot accept two instances of the same test case
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/issue_aggregate.c
Cannot merge issues with different groups
put
%s: ART command %s failed\n
%s: ART get nonce request failed\n
%2x
IOKit returned %x for kSEP_RunAll\n
\t\t--pair <obj>             Factory pairing commands. Requires: --outfile\n
%s: fd_to_buf returned false\n
OSBundleUUID
%lld
securitymode
hash
get-var
\t\t--get-var <app>:<name>            Get value of debug variable\n
\tBare words on the commandline are sent to the SEP as a console command\n
%s: Missing test output file\n
disable
%s: lynx get epochs returned 0x%x
daemonize_xpc_reseed running
Test data can only be passed in or out of a single test\n
Unable to check validity of NULL result
Unable to create a test case result with NULL name
Cannot set the reason for a NULL issue
launch-macos-app
\tROM commands\n
%s: auto load failed\n
IODeviceTree:/arm-io/sep/iop-sep-nub/xART
Bad Input
hilo-accumulate-test-pattern
\t\t--nap                    Nap the SEP NOW!\n
\tCoverage commands\n
\t\t--alloc-dynamic-object \t Request allocation of test Dynamic Scheme3 object\n
enable
%s: pingflood failed\n
\t0x%016llx
hilo-get-lth-transfer-message
\t\t--list-var <app>                  List all debug variables in app\n
%s: must be run as root\n
a:b:c:d:f:g:hkmno:pq:r:s:t:uv:wx:CDFQI:L:NO:PR:T:W:
%s: Failed to initialize gigalocker: %d\n
/tmp/sep_manager_coverage.raw
%s: Missing dump coverage name \n
%s: Set ART command error: malformed hex string provided
%s: Missing or invalid gain test set\n
%s: Bad hash hex string (%d)\n
%s: failed to read the firmware file\n
read failed in fd_to_buf\n
0x%llx
Had to drop an instance of %s (%d)
\t\t--art ctrtest            Counter self-test\n
\t\t--test-all               Run all available tests\n
%s: Could not register SIGINT handler. We may leak an IOKit iterator if interrupted\n
%s: Zero sized input file\n
%s: unexpected return call size\n
%s: Couldn't allocate memory for LTH\n
Unable to add metric to NULL result
%s: invalid UUID\n
set_provisional_ap_value %d\n
/System/Library/Extensions/AppleSEPManager.kext/AppleSEPManager
json
infile
\t\t--outfile <path>         Output file path. \"-\" for stdout\n
\t\t--create <obj>           Create an object in SEP. Requires --size\n
%s: purge system token failed: 0x%x
 merge -o 
\t%s (Flags: %s)\n
%s: Object create failed\n
tz0
Cannot set issue time to 0
suite->_test_cases
pair->_key
get-endpoint-info
\t\t--set-var <app>:<name>:<value>    Set value of debug variable. If the value is out of range of the debug variable (signed or unsigned), throws an error\n
%s: didn't provide slot ID to commit-hash
%s: get endpoint info returned 0x%x\n
sepi absent
tunable-check
set-provisional
%s: error reading from stdin
%s: L4 panic notification returned 0x%x\n
sepfw-loaded
basic_string
Name
patches
hilo-check-gain-test-pattern
%s: Missing name \n
%s: could not allocate data buffer
/mnt7
[PASS] %s\n
Test cases require a name and category (name = %s, category = %s)\n
new-nonce
hilo-expect-gain-failure
hilo-load-dr-lth
\tSMC test command\n
%s: Timeout trying to connect to the SEP\n
%s: Clear ART error: 0x%x\n
chip-id
str
nap
daemonize-update-timer
\tUnit test commands\n
CAN NOT
ART persisted successfully
llvm-cov report failed. Return code was 
result
pingflood
%s: Missing or invalid test offset value\n
%s: Gigalocker initialization failed: %d\n
%s: '%s' is too large for buffer
%s called with slot %u\n
*str
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_statistic.c
\tDebugging and Diagnostic commands\n
%s: test returned failure\n
IODeviceTree
commitSepHash
kill-nonce
%s: Missing slot ID\n
%s: failed to commit AP hash\n
 report 
aggregate_string
Unable to write full json to file
preflight: mix 'n match specified
restore nonce
gigalocker-init
\t\t--wait <file>            Pause for kernel driver to load before failing\n
\t\t--art clear              Clear the persisted ART\n
\t\t--kill-nonce             Request invalidate SEP/OS nonce\n
set
%s: can't find arm-io/sep\n
reseed-xnu-prng
%s: failed to get lynx chip serial number\n
%s: commit hash failed: 0x%x\n
%s: fd_to_buf read more data than max permissible limit (max_len = %d)\n
%s: getLogSize returned error 0x%x\n
%s: error %ld while retrieving path for personalized data\n
WARNING: Unable to read chip_id, assuming SEP has TZ0 alignment requirement\n
/Library/Caches/com.apple.xbs/2E602A5D-2462-492E-87BE-A26C04FCEA67/TemporaryDirectory.WEh7RF/Sources/AppleSEPUtil/libsep_testing/src/sep_testing.c
Debug var command %d failed, ret: 0x%x\n
TEST_NO_DEFAULT
Category %s\n
Unable to open requested file
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_metric.c
Unable to create a statistic bucket with a null name
hilo-update-timer
%s: can't open '%s'\n
%s: rng-dump %ld failed\n
%s: Gigalocker initialization completed\n
rawlog
Filepath must be provided to save to disk
libembeddedtest
wait
%s: ART new-nonce request failed\n
%s: ART invalidate nonce request failed\n
%s: Put %s failed\n
result->_bucket
read-file
\tDynamic Scheme3 test command\n
%s: Missing SMC event count \n
%s: ART query failed\n
/usr/local/bin/kpgo
{\"Name\":\"%s\",\"Instances\":%d,\"Buckets\":{%s}}
img4: payload decode failed
test-input
%s: dump firmware failed\n
%s: Get nonce command error: %x\n
%s: Warning: Incorrect value size for %s property\n
%s: Invalid pair method\n
 becuase it doesnt have any regions to cover
Cannot fail a histogram
set-var
%s: failed to get lynx public key\n
%s: Hilo get LTH transfer attestation failed: 0x%x\n
%s: ROM command error: %x\n
Production Status = %llu\nSecurity Mode     = %llu\n
ctrtest
%s: kSEP_RngDump: returned bad data size %lu
Error class requested does not match anything in enum
hilo-load-lth-raw
hilo-scrt-path
%s: Hilo test LTH transfer attestation had unexpected return value: 0x%x\n
<skipped %d empty entries>\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case.c
\t\t--rawlog                 Dump the mailbox message RAW log without decoding\n
\t\t--put <obj>              Read stdin and write to obj\n
%s: not reading object data from a terminal, re-direct data from another file\n
%s: test command failed\n
ucont-size
IOKit returned %x for kSEP_QueryTests\n
results->_issues
failure
sepi digest
ping
process-info
commitApHash
/usr/bin/llvm-profdata
Embedded Test Version
bucket
get
\t\t--send-smc-events <count> Send <count> test SMC events to SEP\n
\tExample: %s help\n\n
WARNING: iBoot allocated an extremely high amount of ar0 memory!\n
create
\t\t--dealloc-dynamic-object \t Request deallocation of test Dynamic Scheme3 object\n
%s: bad corruption type %s\n
%s: Invalid value for provisional AP slot state\n
%s: Hilo get LTH transfer message failed: 0x%x\n
%s: xART is not supported on platform, skipping initialization\n
input file too large in fd_to_buf (max size %zu)\n
\t\t--slot <slot id>         Set nonce slot to be used to boot the SEP FW that is being loaded \n
%s: No lcrt file provided\n
%s: could not make matching dictionary for '%s'\n
IODeviceTree:/arm-io/sep
%s: New nonce command error: %x\n
vsnprintf returned an error...%d\n
%s: load fw returned 0x%x\n
%s: readFile of %s failed (%d)
statistic->_metrics
bucket->_name
%c%c
\t\t--sepospanic             Force a SEP/OS panic\n
%s: Couldn't open testing output\n
%s: bad gain restriction %s\n
%s: Incorrect %s entry value type\n
%s: lynx get public key returned 0x%x\n
%s: Counter self-test error: 0x%x\n
%s: Minimum good blocks criteria not met\n
test-offset
\t\t--test-run <category>[/<test>]\n
%s: Hilo advance gain restriction phase failed\n
%s: ttyin '\\n' failed
%s: Invalid object name\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/json.c
Unable to check validity of NULL issue
Cannot merge issues with different reasons
Img4DecodePayloadPropertyExistsByTag('rddg') returned %d\n
art-set
\t\t--boot-check <file>      Check whether the installed SEPFW might be bootable WRT the current ART\n
\t\t--rom nop                Send a ROM NOP command\n
\tProvisional AP slot commands (only supported where nonce slots supported)\n
%s: Missing test name\n
%s: find arm-io/sep failed\n
Copied %u bytes to %c%c%c%C\n
%s: boot check failed\n
%s: Failed to generate ROM nonce: %x\n
%s: Get ART command error: 0x%x\n
bootCheck: SEP %s boot with ART\n
-c
%s: could not find SEP service\n
name
{\"Group\":\"%s\",\"Reason\":\"%s\",\"Class\":\"%s\",\"Count\":%d}
%s: couldn't write out Lynx Public Key\n
clear
daemonize_xpc_reseed
Cannot set the time for a NULL issue
embeddedtest_issue_t object is required to create an issue aggregate
%s: lcrt verification failed\n
SEP firmware %spreloaded in memory\n
%s.gl
Cannot pass a histogram
aggregate->_group
hilo-set-gain-restriction
\t\t--get-nonce              Get current SEP/OS nonce\n
%s: Hilo update timer failed: 0x%x\n
%s: dump coverage failed\n
Epoch %lu: 0x%x\n
%s: unexpected result size %lu\n
new_metric
manifest hash
preflight
%s: Raw LTH fetch operation failed: 0x%x\n
%s: couldn't write out Lynx Chip Serial Number\n
Report parsing failed. Check 
%s: Tunable mode must be 'enable' or 'disable'.\n
%s: can't open '%s', errno: %s(%d)\n
%s: hilo_get_lth_transfer_attestation failed: 0x%x\n
%s/%s.gl
WARNING: iBoot allocated an odd number of bytes for ar0 memory!\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_statistic_metric.c
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/issue.c
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/serialization.c
preflight: FAIL: could not parse ART
rng-dump
%s: failed to commit SEP hash\n
status
may
Retrieving old value: 
statistic->_name
service
IOServiceFirstMatch
ucont-offset
%s: can't write to output\n
daemonize_xpc_reseed finished: failure
kSEP_QueryTests returned test_suites_size of 0!\n
statistic_1->_metrics
%s: Warning: can't find /chosen\n
%s: hilo_get_lth_transfer_message_with_manifest failed: 0x%x\n
TEST_DATA_IN
/tmp/sep_manager_coverage.profdata
Unable to pass NULL result
test-run
%s: hilo_get_sik_pub_key failed
Boot slot not provided to load SEPFW, setting to default
embeddedtest: allocation failed for %s (file: %s, line: %d)\n
result->_metrics
Cannot set issue group to NULL
preflight: manifest hash matches, but not checking load
pair
hilo-corrupt-lth
%s: incorrect file size reported\n
Unable to create test case statistic with NULL initial result
hilo-corrupt-lth-transfer-attestation
\t\t--art get                Dump current ART from Memory\n
%s: Missing debug var name \n
%s: failed to show lynx epochs\n
%s: Couldn't find property \"%s\"\n
Categories Found: %s\n
check-boot-size
init_data_protection
%s: Hilo gain restriction set failed\n
%s: can't stat '%s'\n
%s: bad arguments: %u %lu\n
[FAIL] %s\n
crash
\t\t--test-input <file>      Set testing input data\n
%s: can't write '%s'\n
%s: Gigalocker file (%s) exists\n
daemonize_xpc_reseed finished: success
ar0-size
img4: failed to parse ART: %d\n
%s: Couldn't write gain test LTH to %s\n
%s: Couldn't load raw LTH, return value: 0x%x\n
w+
Incomplete Struct
report-code-coverage
%s: No/Illegal outfile provided\n
protected-data-access
WARNING: iBoot did not allocate enough space for scheme2!\n
sep_connect
Successfully parsed ART:
r
ucert-size
%s: can't write attestation (to outfile)\n
%s: unknown corruption type %d\n
Results object must be provided to save to disk
Cannot set the group for a NULL issue
\t\t--ping                   Send a PING operation to the SEP OS\n
\t\t--new-nonce              Request new SEP/OS nonce\n
\t\t                         'value' should be 'enable' or 'disable'.\n
%s: didn't provide slot ID to commit-hash-ap
Slot %u provisional: %d, used: %d\n
Did not see a valid file
%s does not appear to be a supported test category\nCategories Found: %s\n
%s/%s does not appear to be a supported test category\n
Unsupported debug var command (cmd=%d)\n
 | 
new_aggregate
Cannot set issue reason to NULL
\tPairing commands\n
%s: not writing data to a terminal, re-direct data to another file\n
Failed to read input data file\n
sepi allows mix 'n match
hilo-set-gain-param-set
%s,%s
pair->_value
share
hilo-get-lth
%s: cannot get LTH transfer message without scrt path\n
 > 
\t\t--get-provisional \tRequires slot to be passed with --slot\n
%s: can't read '%s'\n
%u %c%c%c%c\n
/
/tmp/sep_manager_report.txt
\t\t--rom status             Get the ROM status\n
\t\t--rom tz0                Send a ROM TZ0 command\n
%s: ROM command %s failed\n
IODeviceTree:/chosen
%s: HiloGetParams failed: %d\n
/tmp/%s_test_results.json
Histogram requires bucket to be set
Error: %s\n
hilo-get-lth-transfer-attestation
outfile
new-rom-nonce
\tOOL Object commands\n
SEP ping #%d\n
0x%016llx:\t0x%016llx
%s: error reading data\n
%s: malloc for message (%lu) failed\n
\t\t--read-file              Test seputil file reading functionality, Requires infile and outfile\n
\t\t--test-output <file>     Set testing output data\n
%s: Missing file path\n
%s: Invalid object/service name\n
%s: couldn't find sik_pub_key_prefix in %s
WARNING: Chip ID 0x%x not specified as having TZ0 alignment requirements or not\n
%s does not appear to be a supported test category\n
Width is invalid
\t\t--help                   Display this usage\n
\t\t--restore <file>         Load <file> as the SEP runtime firmware in restore mode\n
%s: Erase install notification returned 0x%x\n
%s: Failed to allocate memory for out_buffer\n
list-var
\t\t--check-boot-size <file> Compares the TZ/AR sizes in the provided img4 file to the values given by iBoot
%s: Hilo corrupt attestation failed\n
%s: Waiting %d seconds for AppleSEPManager...\n
Shared '%c%c%c%c' with '%c%c%c%c'\n
%s: can't read in message\n
Report parsing was successful.  Results will be written to 
%d
daemonize-reseed
%s: can't read in LTH transfer manifest\n
Unable to open %s
Unable to fail NULL result
bucket_names
Cannot print tests cases for NULL result to syslog
Write Failure
boot-check
alloc-dynamic-object
{\"Info\":{%s},\"Issues\":[%s],\"Test Cases\":[%s]}
highlight
sepospanic
\t\t--commit-hash       Commit the SEP hash of the currently loaded firmware. Requires slot to be passed with --slot where nonce slots supported.\n
%s: Nap failed\n
%s: Couldn't get raw LTH, return value: 0x%x
23
Unknown
\t\t--new-rom-nonce          Request new ROM nonce. Requires --outfile\n
%s: Missing arguments \n
%s: can't read in lcrt\n
TEST_DATA_OUT
load
\t\t--reseed-xnu-prng        Reseed XNU's PRNG by getting entropy out of SEP's TRNG
tz1-size
Successfully set new variable value
aggregate
lynx_get_cpsn
\t\t--report-code-coverage   Output a structured data file with coverage data\n
%s: Missing set provisional state \n
Issue must have a reason
Key and value are required to create info pair.  Key was %s and value was %s\n
counter: %lld\n
preflight: restore nonce matches
test-output
nop
com.apple.driver.AppleSEPManager
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_result.c
result->_name
statistic->_buckets
preflight: manifest hash matches sepi
ERROR: failed to determine utility name: %s\n
%s: ERROR: Invalid option\n
%s: couldn't write out Lynx app hash\n
Unsupported testing command (cmd=%d)\n
metric
issue->_reason
rsep allows mix 'n match
\t\t--share <obj>            Share an object. Requires --service\n
%s: Missing count \n
%s: not writing object data to a terminal, re-direct data to another file\n
%s: pairing failed\n
%s: LTH write to %s failed
Unable to create test case statistic metric with a null name
img4: img4 parse failed\n
%s: Missing object handle \n
Failed to query nonce slot support\n
%s: invalid argument\n
issue
gigalocker-shutdown
test-list
%s: lcrt verification request returned 0x%x\n
get-provisional
\t\t--test-list              List all available tests\n
ucert-offset
%s: SEP/OS panic request returned 0x%x\n
rsep nonce
\t\t--commit-hash-ap    Commit the AP hash of the currently loaded firmware. Requires slot to be passed with --slot where nonce slots supported.\n
\tSystem testing commands\n
%s: version argument 0x%lx is not a valid uint16 value\n
%s: missing UUID \n
%s: Raw LTH didn't have expected value
%s: Provisional AP command missing slot ID\n
%s: unexpected file size (size %lld)
rsep digest
hilo-get-dr-lth
%s: Couldn't open testing input\n
%s: Object size missing/out of range/invalid\n
%s: can't allocate memory for LTH\n
%s: can't read in attestation\n
unknown ROM command
Result did not have pass/fail set
minblocks
dealloc-dynamic-object
OPTIONS:\n\n
\t\t--dump-fw <file>         Dump measurements of installed SEP FW file \n
%s: Invalid/No object size specified\n
%s: Share %s failed\n
bootCheck: Cannot perform boot check on non-ART platform. Assuming OK
AppleSEPManager Code Coverage
%s: Writing to output file failed in read file test\n
suites
{\"Name\":\"%s\",\"Instances\":%d,\"Failure Count\":%d,\"Failure Buckets\":{%s},\"Metrics\":[%s]}
embeddedtest_create_string_from_buffer saw a size > 10000
\"%s\":%d
\t\t%s --test-run test/pass (run the test 'pass' in the category 'test')\n
%s: stdin data too large
%s: Gigalocker file (%s) doesn't exist: %s\n
ar1-size
, 
Unable to create a test case metric with a NULL name...%s\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_suite.c
hilo-lth-transfer-manifest
hilo-advance-gain-restriction-phase
\t\t--rng-dump <count>       Dump specified count bytes worth of data from TRNG\n
IOKit returned %x for kSEP_GetResult\n
Test data input too big\n
size
%s: process info failed\n
%s: fd_to_buf returned NULL in read file test\n
%s: Couldn't get raw LTH, return value: 0x%x\n
%s: Read LTH size is %u, expected %lu\n
/private/xarts
New value is out of range of debug variable [%lld, %lld]\n
subcounters[%lu]: %llu\n
%s (%ld bytes): 
%s: Missing hash\n
Failed to write out the JSON file
{\"Name\":\"%s\",\"Max\":%f,\"Min\":%f,\"Mean\":%f,\"StdDev\":%f,\"Count\":%d}
merged_buckets
%s: failed to load %s in %c%c%c%c mode\n
%s: could not add async match notification\n
Found slot %u in patches IM4R\n
\n%s: Time taken: %lld ns\n
Impossible Value
%s absent\n
%s: Get %s failed\n
sepfw-load-at-boot
Reason cannot be null when failing a test case
l4panic
AppleSEPUtil
Usage: %s ...\n
\tGeneric commands\n
\t\t--restore+art <file>     Load <file> as the SEP runtime firmware in restore mode with ART\n
\t\t--get <obj>              Read obj and write to stdout\n
%s: commit hash returned 0x%x\n
%s: Incorrect sepfw-loaded entry value type\n
sepi nonce
Histogram by time did not have a end time
statistic
Cannot set the class for a NULL issue
\"%s\":\"%s\"
%s: Missing or invalid BIS bits per subpixel type value\n
%s: Failed to allocate memory for fetching mailbox logs\n
\tSlide: 0x%llx\n
%s could not open SEP service, IOServiceOpen returned %d\n
hilo-create-gain-test-lth
\t\t--process-info           Display information for SEP processes\n
%s: Missing or invalid test timeout value\n
%s: Failed to start versioned apps result=0x%x\n
Loading SEP FW in %s with slot %u\n
new_statistic
slot
dump-fw
%s: Unable to parse provisional AP slot state\n
%s: Couldn't read LTH from %s\n
TEST_REQUIRE_ERASE_INSTALL
rsep absent
lynx_get_app_hash
%s: SEP/OS panic notification returned 0x%x\n
[Pass]
\t\t--preflight              Pre-flight load/restore firmware against ART to pre-check for boot failures\n
\t\t--test-offset <value>    Set data transfer offset within input data (default=0)\n
\t\t%s --test-run test (run all tests in the category 'test')\n
%s: ttyin '%c' failed\n
%s: kSEP_ObjRead: returned bad data size %lu
\t UUID: %s\n
%s: can't allocate memory for '%s'\n
tz0-size
sleep hash
remove-system-token-from-art
\t\t--size <size>            Size of object in case requesting object create\n
\t\t                         Valid arguments for <obj>- STCK, SIGN\n
\t\t                         Run a test or set of tests in a category\n
%s: Hilo gain calculation had unexpected return value: 0x%x, hilo_expect_gain_failure: %d\n
%s: No/Illegal infile provided\n
 
preflight: nonce matches, but not checking restore
erase
\t\t--load <file>            Load <file> as the SEP runtime firmware\n
%s: failed to get lynx app hash\n
%s: Hilo load LTH had unexpected return value: 0x%x\n
%s: HILO_BYTE_TO_CORRUPT is not within LTH backup\n
Skipping SEP firmware load
 -arch arm64 > 
\t\t--infile <path>          Input file path if passing in some data\n
Endpoint %d name '%c%c%c%c' ool_in_pages [%u,%u] ool_out_pages [%u,%u]\n
escaped_str
[Fail]
hilo-get-lth-raw
\t\t--service <srvc>         Service handle with which an object is to be shared\n
Failed to update tunable check mode. ret: 0x%x\n
%s: Channel %d sample %u had bad LTH value (expected %u, got %u)\n
%s: malloc for attestation (%lu) failed\n
metric->_name
0123456789abcdef
commit-hash-ap
suite
%s: Missing or invalid version\n
%s: Invalid/No service handle\n
%s: Set ART error: 0x%x\n
/bin/bash
xart_os_uuid
\t\t--pingflood              Ping SEP endlessly\n
%s: Incorrect value size for %s property\n
%s: Warning: Incorrect %s property value type\n
%s: found sik_pub_key_prefix at bad spot in %s
kpgo failed.  Was code coverage enabled at build time? Return code was 
IOKit returned %x for kSEP_RunCat\n
Metrics cannot be added to a histogram
img4: Img4DecodeInit failed: %d\n
img4: extract returned NULL
commit-hash
%s: Missing value \n
SEPUTIL TRNG: %s
could not get the machine's unique identifier, reason: %s
Gigalocker partition does not exist
```
