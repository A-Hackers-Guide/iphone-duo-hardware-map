# `/usr/libexec/seputil`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 204,320 bytes.

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
%s: failed to get lynx public key\n
 merge -o 
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_statistic.c
preflight
test-list
r
%s: Missing or invalid test offset value\n
%s: fd_to_buf returned false\n
Filepath must be provided to save to disk
%s: Hilo gain restriction set failed\n
hilo-test-lth-transfer-attestation
dump-fw
\t\t--pingflood              Ping SEP endlessly\n
\t\t--slot <slot id>         Set nonce slot to be used to boot the SEP FW that is being loaded \n
Unsupported testing command (cmd=%d)\n
img4: couldn't get bool property - fatal
test-all
test-input
hilo-accumulate-test-pattern
\t\t--launch-macos-app <ver> Launch MacOS serving app variant for the specified 16-bit hex version\n
ucert-size
/tmp/sep_manager_coverage.profdata
llvm-cov report failed. Return code was 
restore
l4panic
%u %c%c%c%c\n
%s: read firmware failed\n
OSBundleUUID
Unable to fail NULL result
Cannot set the time for a NULL issue
test_case
hilo-check-gain-test-pattern
%s: failed to commit AP hash\n
commitApHash
daemonize_xpc_reseed
read failed in fd_to_buf\n
IOKit returned %x for kSEP_RunAll\n
Cannot set issue time to 0
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_statistic_bucket.c
\tDebugging and Diagnostic commands\n
%s: Missing name \n
%s: unexpected file size (size %lld)
%s: minblocks out of range\n
\n%s: Time taken: %lld ns\n
%2x
launch-macos-app
%s: Missing or invalid version\n
Slot %u provisional: %d, used: %d\n
/
tz1-size
Usage: %s ...\n
\t\t--read-file              Test seputil file reading functionality, Requires infile and outfile\n
\t\t--preflight              Pre-flight load/restore firmware against ART to pre-check for boot failures\n
%s: Missing or invalid gain test set\n
set_provisional_ap_value %d\n
%s: Get mailbox log failed : %d\n
%s: could not allocate buffer for scrt
/tmp/%s_test_results.json
\tBare words on the commandline are sent to the SEP as a console command\n
%s absent\n
\tSMC test command\n
0x%llx
Unable to create test case statistic metric with a null name
Had to drop an instance of %s (%d)
suite
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case.c
test-run
\t\tExamples:\n
%s: LTH write to %s failed
preflight: manifest hash matches sepi
wait
\t\t--rng-dump <count>       Dump specified count bytes worth of data from TRNG\n
\t\t--create <obj>           Create an object in SEP. Requires --size\n
nop
%s: Couldn't load raw LTH, return value: 0x%x\n
/usr/local/bin/kpgo
 | 
commit-hash
\t\t--minblocks <value>      Optional argument to compare \"--art ctrtest\" good pages against\n
%s: failed to get lynx chip serial number\n
%s: could not make matching dictionary for '%s'\n
%s: hilo_get_sik_pub_key failed
Histogram by time did not have a end time
statistic->_name
issue->_group
hilo-load-lth
\t\t--requestpanic           Force a SEP/OS client requested panic\n
%s: Erase install notification returned 0x%x\n
%s: Gigalocker initialization completed\n
%s: can't read in attestation\n
%s does not appear to be a supported test category\n
Reason cannot be null when failing a test case
Error seen...%s - %s\n
%s: Invalid pair method\n
basic_string
New value is out of range of debug variable [%lld, %lld]\n
pair->_key
outfile
hash
\t\t--art-set <value>        Persist the supplied ART value to storage\n
%s: Hilo load LTH transfer message failed: 0x%x\n
WARNING: Unable to read chip_id, assuming SEP has TZ0 alignment requirement\n
statistic_1->_metrics
results->_issues
process-info
list-var
%s: Waiting %d seconds for AppleSEPManager...\n
 report 
statistic->_metrics
embeddedtest_issue_t object is required to create an issue aggregate
boot-check
test-offset
dealloc-dynamic-object
\t\t--ping                   Send a PING operation to the SEP OS\n
%s: ART new-nonce request failed\n
%s: hilo_get_lth_transfer_message_with_manifest failed: 0x%x\n
gigalocker-shutdown
w
%s: Missing debug var name \n
%s: could not add async match notification\n
[FAIL] %s\n
Result did not have pass/fail set
\t\t--pair <obj>             Factory pairing commands. Requires: --outfile\n
%s: bad corruption type %s\n
%s: didn't provide slot ID to commit-hash
Key and value are required to create info pair.  Key was %s and value was %s\n
subcounters[%lu]: %llu\n
com.apple.driver.AppleSEPManager
Embedded Test Version
%s (%ld bytes): 
hilo-get-lth
hilo-set-gain-param-set
%s: can't find arm-io/sep\n
%s: lynx get public key returned 0x%x\n
%s: can't allocate memory for '%s'\n
Test data can only be passed in or out of a single test\n
%s could not open SEP service, IOServiceOpen returned %d\n
rsep nonce
get
hilo-lth-transfer-manifest
%s: bad arguments: %u %lu\n
IODeviceTree:/chosen
 becuase it doesnt have any regions to cover
result->_name
[Pass]
commit-hash-ap
%s: failed to get lynx app hash\n
IOServiceFirstMatch
%s: Read LTH size is %u, expected %lu\n
IOKit returned %x for kSEP_QueryTests\n
Unable to create a statistic bucket with a null name
%s: Couldn't find property \"%s\"\n
load
\t\t--outfile <path>         Output file path. \"-\" for stdout\n
\t\t--restore <file>         Load <file> as the SEP runtime firmware in restore mode\n
IOKit returned %x for kSEP_GetResult\n
Impossible results class %d\n
hilo-get-lth-transfer-attestation
%s: ART get nonce request failed\n
%s: commit hash failed: 0x%x\n
%s: Minimum good blocks criteria not met\n
%s: can't read in scrt\n
input file too large in fd_to_buf (max size %zu)\n
Unable to write full json to file
img4: extract returned NULL
%s: Failed to start versioned apps result=0x%x\n
Loading SEP FW in %s with slot %u\n
Unit test results only accept pass fail test cases
Cannot set issue reason to NULL
/usr/bin/llvm-profdata
suites
Unable to check validity of NULL result
suite->_test_cases
\t\t--art ctrtest            Counter self-test\n
%s: Provisional AP command failed\n
Issue must have a group
%s: Clear ART error: 0x%x\n
%s: No/Illegal infile provided\n
%s does not appear to be a supported test category\nCategories Found: %s\n
hilo-corrupt-lth
IODeviceTree:/arm-io/sep
\tSlide: 0x%llx\n
share
hilo-advance-gain-restriction-phase
%s: version argument 0x%lx is not a valid uint16 value\n
%s: Object size missing/out of range/invalid\n
name
%s: Missing object handle \n
%s: Writing to output file failed in read file test\n
Report parsing was successful.  Results will be written to 
Unsupported debug var command (cmd=%d)\n
[PASS] %s\n
highlight
hilo-load-dr-lth
%s: Couldn't get raw LTH, return value: 0x%x
0x%016llx:\t0x%016llx
/private/xarts
Cannot merge statistics with mismatching names
results->_info
Had to drop an issue (%d)
Bad Input
Impossible Value
rsep absent
\t\t--report-code-coverage   Output a structured data file with coverage data\n
%s: test returned failure\n
%s: prop %s val 0x%x\n
%s: can't read in LTH transfer manifest\n
%s: img4 dump failed\n
, 
Metrics cannot be added to a histogram
aggregate
daemonize-update-timer
\t\t                         'value' should be 'enable' or 'disable'.\n
%s: Missing value \n
Failed to query nonce slot support\n
\t0x%016llx
%s: Get ART command error: 0x%x\n
v16@?0^{_xpc_activity_s=}8
TEST_DATA_OUT
\t\t--art get                Dump current ART from Memory\n
AppleSEPManager
%s: commit hash returned 0x%x\n
%s: can't open '%s' for writing\n
%s.gl
tz0-size
Failed to get debug variable\n
statistic->_buckets
Img4DecodePayloadPropertyExistsByTag('rddg') returned %d\n
%s: Raw LTH fetch operation failed: 0x%x\n
%s: No/Illegal outfile provided\n
Counter self-test result: %u/%u good\n
IOKit returned %x for kSEP_RunCat\n
new_aggregate
\tProvisional AP slot commands (only supported where nonce slots supported)\n
%s: rng-dump %ld failed\n
has-art
%s: can't read in lcrt\n
%s: get endpoint info returned 0x%x\n
results->_statistics
embeddedtest_create_string_from_buffer saw a size > 10000
raw ART: 
set-provisional
\tUnit test commands\n
\t\t--list-var <app>                  List all debug variables in app\n
%s: Raw LTH didn't have expected value
%s: Set ART error: 0x%x\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/json.c
restore nonce
rng-dump
hilo-get-lth-raw
\t\t--set-var <app>:<name>:<value>    Set value of debug variable. If the value is out of range of the debug variable (signed or unsigned), throws an error\n
ERROR: failed to determine utility name: %s\n
%s: not writing object data to a terminal, re-direct data to another file\n
%s: boot check failed\n
%s: Hilo load LTH had unexpected return value: 0x%x\n
\t\t--set-provisional <value> \tSet the provisional state of AP slot to 1 (provisional) or 0 (not provisional). Requires slot to be passed with --slot.\n
%s: Missing file path\n
%s: Put %s failed\n
%s: couldn't write out Lynx app hash\n
%s: error reading data\n
%s: couldn't find sik_pub_key_prefix in %s
daemonize_xpc_reseed finished: success
\t%s (Flags: %s)\n
%s: failed to load %s in %c%c%c%c mode\n
 > 
rawlog
show-epochs
%s: ping failed\n
%s called with slot %u\n
%s: kSEP_ObjRead: returned bad data size %lu
%s: Gigalocker file (%s) exists\n
%s: can't allocate memory for LTH\n
%s/%s.gl
has_system_token
%s: HILO_BYTE_TO_CORRUPT is not within LTH backup\n
%s: No display params when expected!\n
Report parsing failed. Check 
{\"Name\":\"%s\",\"Instances\":%d,\"Buckets\":{%s}}
results
issue->_reason
Issue cannot have a time of less than or equal to 0
\tExample: %s --wait --load /path/to/foo\n
\tART commands\n
%s: '%s' is too large for buffer
%s: couldn't write out Lynx Chip Serial Number\n
SEP firmware %spreloaded in memory\n
%s: xART OS UUID setup failed: %d\n
Cannot fail a histogram
Cannot set the group for a NULL issue
%s: not writing data to a terminal, re-direct data to another file\n
%s: test command failed\n
%s: ART query failed\n
Skipping SEP firmware load
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_result.c
sepi nonce
sepi absent
a:b:c:d:f:g:hkmno:pq:r:s:t:uv:wx:CDFQI:L:NO:PR:T:W:
Debug var command %d failed, ret: 0x%x\n
clear
%s: Incorrect value size for sepfw-loaded property\n
Cannot merge issues with different groups
preflight: nonce matches, but not checking restore
hilo-load-lth-transfer-message
daemonize-reseed
\t\t--sepospanic             Force a SEP/OS panic\n
%s: security mode query failed\n
%s: Set ART command error: malformed hex string provided
%s: xART is not supported on platform, skipping initialization\n
Cannot set the class for a NULL issue
\t\t--get <obj>              Read obj and write to stdout\n
%s: Failed to initialize gigalocker: %d\n
%s: found sik_pub_key_prefix at bad spot in %s
/Library/Caches/com.apple.xbs/2E602A5D-2462-492E-87BE-A26C04FCEA67/TemporaryDirectory.WEh7RF/Sources/AppleSEPUtil/libsep_testing/src/sep_testing.c
bucket->_name
%s: missing UUID \n
Shared '%c%c%c%c' with '%c%c%c%c'\n
/tmp/sep_manager_coverage.raw
IOKit returned %x for kSEP_RunHandle\n
counter: %lld\n
lynx_get_cpsn
hilo-set-gain-restriction
%s: not reading object data from a terminal, re-direct data from another file\n
:
%s: ERROR: Invalid option\n
%s: cannot get LTH transfer message without scrt path\n
IODeviceTree
pingflood
\t\t--nap                    Nap the SEP NOW!\n
\t\t--test-offset <value>    Set data transfer offset within input data (default=0)\n
%s: Unable to parse provisional AP slot state\n
was not 
%s: unexpected return call size\n
%s: unexpected result size %lu\n
Results object must be provided to save to disk
sepi digest
\t\t--process-info           Display information for SEP processes\n
\t\t--wait <file>            Pause for kernel driver to load before failing\n
bucket_names
Issue must have a reason
\t\t--help                   Display this usage\n
%s: Missing hash\n
%s: failed to commit SEP hash\n
%s: malloc for message (%lu) failed\n
Boot slot not provided to load SEPFW, setting to default
realloc failed in fd_to_buf for size %zu\n
check-boot-size
art-set
\t\t--kill-nonce             Request invalidate SEP/OS nonce\n
%s: lcrt verification request returned 0x%x\n
slot
\tSystem testing commands\n
\tExample: %s help\n\n
%s: Tunable mode must be 'enable' or 'disable'.\n
%s: dump firmware failed\n
%s: Hilo test LTH transfer attestation had unexpected return value: 0x%x\n
%s: ttyin '\\n' failed
libembeddedtest
%s: Hilo update timer failed: 0x%x\n
%s: Couldn't get raw LTH, return value: 0x%x\n
/System/Library/Extensions/AppleSEPManager.kext/AppleSEPManager
Successfully parsed ART:
minblocks
%s: inconsistent mailbox Log size : %d\n
bootCheck: SEP %s boot with ART\n
%s %s/%s\n
Unit test results cannot accept two instances of the same test case
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/serialization.c
kill-nonce
%s: Missing SMC event count \n
Failed to update tunable check mode. ret: 0x%x\n
%s: stdin data too large
%s: Incorrect %s entry value type\n
%s: Incorrect sepfw-loaded entry value type\n
 -instr-profile=
Width is invalid
\t\t--get-provisional \tRequires slot to be passed with --slot\n
%s: Share %s failed\n
%s: Warning: can't find /chosen\n
Skipping 
%s: Missing slot ID\n
%s: Get %s failed\n
 for more detail
aggregate->_reason
%s: ART invalidate nonce request failed\n
Found slot %u in patches IM4R\n
img4: failed to parse ART
read-file
lynx_get_pub_key
disable
%s: failed to read the firmware file\n
Cannot merge issues with different reasons
\t\t--restore+art <file>     Load <file> as the SEP runtime firmware in restore mode with ART\n
%s: Missing set provisional state \n
%s: ART command %s failed\n
%s: Warning: Incorrect value size for %s property\n
Hilo update timer failed: 0x%x
result
result->_metrics
Unable to create a test case metric with a NULL name...%s\n
\t\t--rom nop                Send a ROM NOP command\n
%s: failed to notify SEP/OS about erase install\n
%s: Object create failed\n
%s: error reading from stdin
%s: L4 panic notification returned 0x%x\n
%s: SEP/OS panic notification returned 0x%x\n
%s: Warning: Incorrect %s property value type\n
%s: Couldn't write gain test LTH to %s\n
put
%s: Missing sub-command\n
%s: didn't provide slot ID to commit-hash-ap
%s: Hilo accumulate test pattern failed: 0x%x\n
<skipped %d empty entries>\n
Production Status = %llu\nSecurity Mode     = %llu\n
%s: Failed to allocate memory for out_buffer\n
%s: couldn't write out LTH transfer message\n
test-timeout
hilo-get-dr-lth
AppleSEPUtil
\t\t--securitymode           Request SEP effective production status and security mode\n
\t\t--test-timeout <value>   Set the default delay in milliseconds to wait for test completion (default=120000)\n
ucont-size
daemonize_xpc_reseed finished: failure
may
\t\t--dump-fw <file>         Dump measurements of installed SEP FW file \n
\t\t--new-nonce              Request new SEP/OS nonce\n
\t\t%s --test-run test/pass (run the test 'pass' in the category 'test')\n
%s: Invalid/No service handle\n
%s: ROM command error: %x\n
Created '%c%c%c%c' of size %u\n
%s: can't read in message\n
ERR: could not get the machine's unique identifier, reason: %s\n
help
\t\t--commit-hash       Commit the SEP hash of the currently loaded firmware. Requires slot to be passed with --slot where nonce slots supported.\n
%s: Missing test name\n
chip-id
Categories Found: %s\n
Failed to write output data file\n
Retrieving old value: 
Unable to open requested file
rsep digest
\t\t--send-smc-events <count> Send <count> test SMC events to SEP\n
%s: must be run as root\n
%s: Hilo corrupt attestation failed\n
%s: Incorrect value size for %s property\n
%s: couldn't write out Lynx Public Key\n
%s: HiloGetParams failed: %d\n
-c
nap
alloc-dynamic-object
SEP ping #%d\n
%s: fd_to_buf read more data than max permissible limit (max_len = %d)\n
%s: ERROR: %d\n
Copied %u bytes to %c%c%c%C\n
TEST_REQUIRE_ERASE_INSTALL
Failed to read input data file\n
\t\t--dealloc-dynamic-object \t Request deallocation of test Dynamic Scheme3 object\n
%s: Missing arguments \n
%s: incorrect file size reported\n
Category %s\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_suite.c
Test cases require a name and category (name = %s, category = %s)\n
pair->_value
img4: failed to parse ART: %d\n
0123456789abcdef
\t\t--reseed-xnu-prng        Reseed XNU's PRNG by getting entropy out of SEP's TRNG
%s: find arm-io/sep failed\n
json
{\"Group\":\"%s\",\"Reason\":\"%s\",\"Class\":\"%s\",\"Count\":%d}
TEST_DATA_IN
aggregate_string
Cannot set issue group to NULL
Unknown
\tDynamic Scheme3 test command\n
%s: can't write attestation (to outfile)\n
Did not see a valid file
metric
Unable to create test case statistic with NULL initial result
xart_os_uuid
%s: unknown corruption type %d\n
ART persisted successfully
i24@?0^{?=Q{?=*Q}}8^B16
\"%s\":\"%s\"
new-rom-nonce
art
test-output
\tGeneric commands\n
\t\t                         Run a test or set of tests in a category\n
%s: ERROR: At least one option required\n
%s: Missing test output file\n
%s: invalid argument\n
hilo-scrt-path
%s: can't read '%s'\n
%d
statistic
%s,%s
issue
%s: Missing or invalid BIS bits per subpixel type value\n
%s: Gigalocker initialization failed: %d\n
%s: can't write to output\n
Error: %s\n
%s: invalid UUID\n
Metric name cannot be null
Cannot print tests cases for NULL result to syslog
[Fail]
service
dump-cov
\t\t--load <file>            Load <file> as the SEP runtime firmware\n
%s: could not allocate data buffer
ART cleared from storage
WARNING: Chip ID 0x%x not specified as having TZ0 alignment requirements or not\n
{\"Name\":\"%s\",\"Max\":%f,\"Min\":%f,\"Mean\":%f,\"StdDev\":%f,\"Count\":%d}
%s: Failed to connect to sep\n
%s: Invalid/No object size specified\n
%s: getLogSize returned error 0x%x\n
str
\t\t--art clear              Clear the persisted ART\n
\t\t--test-list              List all available tests\n
\t\t--alloc-dynamic-object \t Request allocation of test Dynamic Scheme3 object\n
%s: process info failed\n
%s: Hilo get LTH transfer attestation failed: 0x%x\n
%s: Failed to generate ROM nonce: %x\n
\t\t--get-nonce              Get current SEP/OS nonce\n
\t\t%s --test-run test (run all tests in the category 'test')\n
%s: Couldn't populate gain test LTH: %d\n
w+
Incomplete Struct
sleep hash
should-be-system-token
\t\t--dump-cov <app>      Dump and reset coverage counters to object\n
%s: Missing debug var new value \n
%s: Provisional AP command missing slot ID\n
%s: Zero sized input file\n
Didn't find snid in patches IM4R, using default slot %u\n
hilo-load-lth-raw
set-var
%s: Missing output file\n
Unable to open %s
tunable-check
\t\t--l4panic                Force an L4 panic\n
%s: bad gain restriction %s\n
%s: lynx get epochs returned 0x%x
%s: auto load failed\n
%s: readFile of %s failed (%d)
%s: purge system token failed: 0x%x
%s: Missing or invalid test timeout value\n
%s: Data out size missing/out of range\n
WARNING: iBoot allocated an odd number of bytes for ar0 memory!\n
OPTIONS:\n\n
\t\t--rom tz0                Send a ROM TZ0 command\n
%s: SEP/OS panic request returned 0x%x\n
IODeviceTree:/arm-io/sep/iop-sep-nub/xART
securitymode
sepospanic
\t\t--size <size>            Size of object in case requesting object create\n
set
%s: Bad hash hex string (%d)\n
%s: Hilo get LTH transfer message failed: 0x%x\n
Kernel message log has %llu entries\n
%s: New nonce command error: %x\n
img4: Img4DecodeInit failed: %d\n
infile
\tROM commands\n
%s: Purge system token failed\n
ucert-offset
sepfw-loaded
Sources/AppleSEPManager
\t\t--check-boot-size <file> Compares the TZ/AR sizes in the provided img4 file to the values given by iBoot
/mnt7
lcrt_verify
%s: Failed to allocate memory for fetching mailbox logs\n
crash
aggregate->_group
\t\t--service <srvc>         Service handle with which an object is to be shared\n
%c%c
%s: lynx get app hash returned 0x%x\n
%lld
vsnprintf returned an error...%d\n
ping
hilo-check-gain-test-lth
\t\t                         Valid arguments for <obj>- STCK, SIGN\n
\t\t--get-var <app>:<name>            Get value of debug variable\n
%s: lynx get chip serial number returned 0x%x\n
ar0-size
preflight: FAIL: could not parse ART
hilo-expect-gain-failure
hilo-update-timer
%s: Hilo advance gain restriction phase failed\n
%s: Timeout trying to connect to the SEP\n
%s: kSEP_RngDump: returned bad data size %lu
unknown ROM command
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/issue.c
preflight: mix 'n match specified
restore+art
%s: mailbox raw log print failed\n
%s: could not get master port\n
/bin/bash
ar1-size
result->_bucket
Cannot merge statistics with mismatching classes
%s: Couldn't open testing input\n
%s: No lcrt file provided\n
daemonize_xpc_reseed running
Failed to write out the JSON file
Unable to check validity of NULL issue
img4: img4 parse failed\n
requestpanic
%s: dump coverage failed\n
SEP status 0x%llx\n
%s: Get nonce command error: %x\n
%s: can't read in infile\n
Unable to add metric to NULL result
%s: pingflood failed\n
%s: ttyin ' ' failed\n
WARNING: iBoot allocated an extremely high amount of ar0 memory!\n
new_statistic
Cannot set the reason for a NULL issue
preflight: manifest hash matches, but not checking load
\t\t--infile <path>          Input file path if passing in some data\n
%s: can't write '%s'\n
\t\t--rom status             Get the ROM status\n
\t\t--test-output <file>     Set testing output data\n
\t\t--tunable-check <value>  Enable or disable tunable check mode.\n
%s: Invalid object name\n
%s: Couldn't read LTH from %s\n
Test data input too big\n
*str
patches
get-var
%s: Invalid value for provisional AP slot state\n
status
tz0
%s: Security mode command error: %x\n
Endpoint %d name '%c%c%c%c' ool_in_pages [%u,%u] ool_out_pages [%u,%u]\n
kSEP_QueryTests returned test_suites_size of 0!\n
remove-system-token-from-art
%s: lcrt verification failed\n
%s: ttyin '%c' failed\n
ucont-offset
 
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_statistic_metric.c
Unable to create a test case result with NULL name
{\"Name\":\"%s\",\"Instances\":%d,\"Failure Count\":%d,\"Failure Buckets\":{%s},\"Metrics\":[%s]}
preflight: FAIL: could not parse img4
\tFirmware commands\n
\t\t--test-all               Run all available tests\n
%s: Nap failed\n
%s: failed to show lynx epochs\n
%s: error %ld while retrieving path for personalized data\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/test_case_metric.c
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/info_pair.c
%s: Channel %d sample %u had bad LTH value (expected %u, got %u)\n
%s: Couldn't allocate memory for LTH\n
IODeviceTree:/arm-io/sep/iop-sep-nub/Sandcat
/usr/bin/llvm-cov
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/results.c
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/issue_aggregate.c
img4: payload decode failed
preflight: restore nonce matches
rom
size
\t\t--put <obj>              Read stdin and write to obj\n
%s: ROM command %s failed\n
Epoch %lu: 0x%x\n
Unable to pass NULL result
%s: malloc for attestation (%lu) failed\n
metric->_name
23
\t\t--share <obj>            Share an object. Requires --service\n
%s: No SEP present on this device\n
AppleSEPManager Code Coverage
IODeviceTree:/arm-io/sep/iop-sep-nub
hilo-create-gain-test-lth
%s: Hilo get LTH failed: 0x%x\n
\tPairing commands\n
%s: Couldn't open testing output\n
enable
%s: Hilo gain calculation had unexpected return value: 0x%x, hilo_expect_gain_failure: %d\n
%s: fd_to_buf returned NULL in read file test\n
sep_connect
Cannot merge issues with different classes
bucket
\t\t--boot-check <file>      Check whether the installed SEPFW might be bootable WRT the current ART\n
%s: Missing count \n
%s: can't stat '%s'\n
Histogram requires bucket to be set
\t\t--commit-hash-ap    Commit the AP hash of the currently loaded firmware. Requires slot to be passed with --slot where nonce slots supported.\n
\tOOL Object commands\n
\tCoverage commands\n
%s: can't open '%s', errno: %s(%d)\n
%s: hilo_get_lth_transfer_attestation failed: 0x%x\n
%s/%s does not appear to be a supported test category\n
Cannot pass a histogram
merged_buckets
sepi allows mix 'n match
get-provisional
%s: Missing test input file\n
defaultInit
\t UUID: %s\n
 -arch arm64 > 
escaped_str
Name
reseed-xnu-prng
new-nonce
init_data_protection
%s: can't open '%s'\n
%s: pairing failed\n
ctrtest
protected-data-access
%s: couldn't write out attestation\n
report-code-coverage
\t\t--new-rom-nonce          Request new ROM nonce. Requires --outfile\n
/tmp/sep_manager_report.txt
WARNING: iBoot did not allocate enough space for scheme2!\n
/Library/Caches/com.apple.xbs/1088A810-8A60-4766-A266-A5E8F3EF91BB/TemporaryDirectory.Lx5cYy/Sources/libembeddedtest/Framework/Source/filesystem.c
gigalocker-init
bootCheck: Cannot perform boot check on non-ART platform. Assuming OK
%s: could not find SEP service\n
\"%s\":%d
rsep allows mix 'n match
hilo-corrupt-lth-transfer-attestation
commitSepHash
%s: Counter self-test error: 0x%x\n
sepfw-load-at-boot
embeddedtest: allocation failed for %s (file: %s, line: %d)\n
failure
hilo-get-lth-transfer-message
%s: Missing dump coverage name \n
%s: Invalid object/service name\n
%s: Could not register SIGINT handler. We may leak an IOKit iterator if interrupted\n
%s: can't write out_buffer (to outfile)\n
kpgo failed.  Was code coverage enabled at build time? Return code was 
Successfully set new variable value
Error class requested does not match anything in enum
manifest hash
erase
pair
\t\t--test-run <category>[/<test>]\n
%s: load fw returned 0x%x\n
%s: Gigalocker file (%s) doesn't exist: %s\n
 because coverage was 0%
TEST_NO_DEFAULT
get-nonce
get-endpoint-info
\t\t--test-input <file>      Set testing input data\n
{\"Info\":{%s},\"Issues\":[%s],\"Test Cases\":[%s]}
Write Failure
lynx_get_app_hash
create
\t\t--rawlog                 Dump the mailbox message RAW log without decoding\n
CAN NOT
new_metric
Gigalocker partition does not exist
SEPUTIL TRNG: %s
could not get the machine's unique identifier, reason: %s
```
