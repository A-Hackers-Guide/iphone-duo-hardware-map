# `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 194,784 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 4056)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (9)

- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication (compatibility version 1.0.0, current version 64578.104.1, weak)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.AppleNVMeEAN.allow</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>identity</string>
		<string>spi</string>
	</array>
	<key>com.apple.ULLAConcierge.xpc</key>
	<true/>
	<key>com.apple.afk.user</key>
	<true/>
	<key>com.apple.aop.user-client.full-access</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.centaurid.xpc</key>
	<true/>
	<key>com.apple.coretelephony.Identity.get</key>
	<true/>
	<key>com.apple.developer.driverkit.userclient-access</key>
	<array>
		<string>com.apple.driver.AppleCentauriControl</string>
	</array>
	<key>com.apple.driver.AirshipDaleBasebandControlInterface.user-access</key>
	<true/>
	<key>com.apple.driver.AppleBasebandPCI.user-access</key>
	<true/>
	<key>com.apple.driver.AppleBasebandPCIControl.user-access</key>
	<true/>
	<key>com.apple.driver.AppleConvergedIPCICEBB.user-access</key>
	<true/>
	<key>com.apple.driver.AppleConvergedIPCICEBBControl.user-access</key>
	<true/>
	<key>com.apple.keystore.fdr-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.nfcd.info</key>
	<true/>
	<key>com.apple.nvmetunnel.allow</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.private.AppleKMPEndpoint.user-access</key>
	<true/>
	<key>com.apple.private.AppleSSMAEndpoint.user-access</key>
	<true/>
	<key>com.apple.private.AppleSSMAService.user-access</key>
	<true/>
	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
	<true/>
	<key>com.apple.private.IOPortTransportAIDBusUserClient.access</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>AmbientLightSensorSerialNumber</string>
		<string>ArcModuleSerialNumber</string>
		<string>ArrowChipID</string>
		<string>ArrowUniqueChipID</string>
		<string>AttestationUniqueDeviceID</string>
		<string>AWDID</string>
		<string>BasebandBoardSnum</string>
		<string>BasebandChipId</string>
		<string>BasebandSerialNumber</string>
		<string>BasebandUniqueId</string>
		<string>BluetoothAddress</string>
		<string>BluetoothAddressData</string>
		<string>BootManifestHash</string>
		<string>CarrierBundleInfoArray</string>
		<string>CompassCalibration</string>
		<string>CompassCalibrationDictionary</string>
		<string>ConfigNumber</string>
		<string>CoverglassSerialNumber</string>
		<string>DiagData</string>
		<string>DieId</string>
		<string>DisplayDriverICChipID</string>
		<string>EthernetMacAddress</string>
		<string>EthernetMacAddressData</string>
		<string>EUICCChipID</string>
		<string>FrontFacingCameraModuleSerialNumber</string>
		<string>FrontFacingIRCameraModuleSerialNumber</string>
		<string>FrontFacingIRStructuredLightProjectorModuleSerialNumber</string>
		<string>IceFallID</string>
		<string>IntegratedCircuitCardIdentifier</string>
		<string>IntegratedCircuitCardIdentifier2</string>
		<string>InternationalMobileEquipmentIdentity</string>
		<string>InternationalMobileEquipmentIdentity2</string>
		<string>InverseDeviceID</string>
		<string>JasperSerialNumber</string>
		<string>LunaFlexSerialNumber</string>
		<string>LynxIdentifier</string>
		<string>LynxPublicKey</string>
		<string>LynxSerialNumber</string>
		<string>MesaSerialNumber</string>
		<string>MLBSerialNumber</string>
		<string>MobileEquipmentIdentifier</string>
		<string>MobileEquipmentInfoBaseId</string>
		<string>MobileEquipmentInfoBaseProfile</string>
		<string>MobileEquipmentInfoBaseVersion</string>
		<string>MobileEquipmentInfoCSN</string>
		<string>MobileEquipmentInfoDisplayCSN</string>
		<string>MultiLynxPublicKeyArray</string>
		<string>MultiLynxSerialNumberArray</string>
		<string>NandControllerUID</string>
		<string>PanelSerialNumber</string>
		<string>PhoneNumber</string>
		<string>PhoneNumber2</string>
		<string>PintoMacAddress</string>
		<string>PintoMacAddressData</string>
		<string>ProvisioningUniqueDeviceID</string>
		<string>ProximitySensorCalibration</string>
		<string>ProximitySensorCalibrationDictionary</string>
		<string>RawPanelSerialNumber</string>
		<string>RearFacingCameraModuleSerialNumber</string>
		<string>RearFacingSuperWideCameraModuleSerialNumber</string>
		<string>RearFacingTelephotoCameraModuleSerialNumber</string>
		<string>RemoteBluetoothAddress</string>
		<string>RemoteBluetoothAddressData</string>
		<string>RosalineSerialNumber</string>
		<string>RoswellChipID</string>
		<string>SavageChipID</string>
		<string>SavageInfo</string>
		<string>SavageSerialNumber</string>
		<string>SavageUID</string>
		<string>ScreenSerialNumber</string>
		<string>SecondaryBluetoothMacAddress</string>
		<string>SecondaryBluetoothMacAddressData</string>
		<string>SecondaryEthernetMacAddress</string>
		<string>SecondaryEthernetMacAddressData</string>
		<string>SecondaryWifiMacAddress</string>
		<string>SecondaryWifiMacAddressData</string>
		<string>SecureElementID</string>
		<string>SerialNumber</string>
		<string>SysCfg</string>
		<string>SysCfgDict</string>
		<string>ThreadRadioMacAddress</string>
		<string>ThreadRadioMacAddress64Bit</string>
		<string>ThreadRadioMacAddress64BitData</string>
		<string>ThreadRadioMacAddressData</string>
		<string>TopModuleAuthChipID</string>
		<string>TristarID</string>
		<string>UniqueChipID</string>
		<string>UniqueDeviceID</string>
		<string>UniqueDeviceIDData</string>
		<string>WifiAddress</string>
		<string>WifiAddressData</string>
		<string>WirelessBoardSnum</string>
		<string>YonkersChipID</string>
		<string>YonkersSerialNumber</string>
		<string>YonkersUID</string>
	</array>
	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.applesepmanager.allow</key>
	<true/>
	<key>com.apple.private.applesmc.user-access</key>
	<true/>
	<key>com.apple.private.domain-extension</key>
	<true/>
	<key>com.apple.private.ioavfamily.user-access-displaymemory</key>
	<true/>
	<key>com.apple.private.security.bootpolicy</key>
	<true/>
	<key>com.apple.private.set-exception-port</key>
	<true/>
	<key>com.apple.private.xpc.domain-extension</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleTCONControlUserClient</string>
		<string>IOAVDisplayMemoryUserClient</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AFKEndpointInterfaceUserClient</string>
		<string>AppleBasebandPCIUserClient</string>
		<string>AppleBasebandUserClient</string>
		<string>AppleBiometricServicesUserClient</string>
		<string>AppleKMPEndpointUserClient</string>
		<string>AppleNVMeEANUC</string>
		<string>AppleSEPUserClient</string>
		<string>AppleSMCClient</string>
		<string>AppleSPUDurantDriverUserClient</string>
		<string>AppleSSMAEndpointUserClient</string>
		<string>AppleSSMAServicesUserClient</string>
		<string>AppleStockholmControlUserClient</string>
		<string>IOAppleConvergedIPCBBUserClient</string>
		<string>IOPortTransportAIDBusUserClient</string>
		<string>IOUserUserClient</string>
	</array>
	<key>com.apple.stockholm.kext.entitlement</key>
	<true/>
</dict>
</plist>
```

## Objective-C (12 classes, 5 protocols)

Classes: `NSArray`, `NSData`, `NSError`, `NSNumber`, `NSString`, `ServiceDelegate`, `ZhuGeCache`, `ZhuGeInternalSupportAssistant`, `ZhuGeLockerService`, `ZhuGeService`, `ZhuGeSingletonService`, `ZhuGeSupportAssistant`

Protocols: `NSObject`, `NSXPCListenerDelegate`, `ZhuGeInternalServiceProtocol`, `ZhuGeRestoreLogProtocol`, `ZhuGeServiceProtocol`

## Strings (891)

```
softlink:r:path:/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage
Error Customized
Name of queried sysconfig key might be wrong
Current XPC connection is not entitled for key \"%@\"!
Maybe unsupported lockdown domain, key or maybe some underlying issue in lockdown daemon
In bulk query, query key: \"%@\" from %@entrusted MG
-restore
Entry %@ doesn't contain a valid personalized image type
File Open Failed
PropertyList Serialization Failed
Received key: \"%@\"
-[ZhuGeService setInternalMGKey:getValueAndError:]
Binary Images:
Failed to insert send right for expcetion port, error %d(%s)!
Issue Underlying
Key of dictionary is redundant
Specific function isn't supported in current OS or environment.
<%@ %@(%@)>
registerCrashReporter
%-21s%s [%d]
Unsupported ARM thread state!
Some internal issues happened when converting data
Please check if you really want to try this function in current OS or environment
+[ZhuGeInternalSupportAssistant getDylibHandlerWithError:]
========== ABORT: set signals action failed ========================
/usr/local/lib/libcryptex.dylib
IO Service Mismatching
Length of some object is unexpected
Entitlement Mismatched
SIGSYS
The data indexed by the indexArray is not valid
+[ZhuGeInternalSupportAssistant getInternalSupportPath]
Failed to find class symbol for \"%@\" with error: %s!
Failed to have shared instance for \"%@\"!
FDR API Failed
+[NSNumber(ZhuGe) integerFromData:size:truncate:isSigned:needSwap:]
catch_mach_exception_raise_state
x86_64
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCache.m
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_2
CLI Option Unsupported
Failed to get internal service proxy for internal key \"%@\"!
sppci_model
OBJC_CLASS_$_ZhuGeInternalArmory
Process:
Exception Type:
Quotation \"%c\" is not paired in command \"%@\"!
Retrieving unchanged internal supported path: %@
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_2
:
Failed to get proc info, error %d(%s)!
MGkey pointer is nil!
Option or input value is not in defined range
ZhuGe exception server does not support catch_mach_exception_raise_state!
EXC_ARITHMETIC
The ACE command returns an error
Initialization Failed
We may need to check with libSMC together
Value Out Of Range
Please make sure the key string is correct
Please check sysdiagnose for more detail
ZhuGeLog
Failed to get backtrace symbols!
Please check whether there is any underlying isse in the decoding API.
Some pointer shall not be NULL
Pattern string can not cover the case
ZhuGe service connected for current connection from pid %@
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_4
========== END: caught a mach exception ==============================
SIGPROF
iCEK
In bulk query, query key: \"%@\" in %@entrusted way
(null)
%@ failed to provide a proxy with error : %@!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCrashReporter.m
Failed to destruct exception port!
Failed to decode with proper API
The dylib does not exists or too old version
JSON String Invalid
Operation is not done in certain time
com.apple.ZhuGe.ZhuGeCrashReporter.printCrash
kern.osversion
createExceptionPort
IO Entry Not Found
Memory is not enough
OS Unsupported
Didn't find the expected path
ZhuGe service bridge-connected for current connection from pid %@
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke
Code Type:
ZhuGe is running well
Failed to create IORegistryEntry iterator
%s: 
???
%s ERR: Restore log connection error: %@
========== End: caught a BSD signal %d(%s) ==================
Entry %@ is not a dictionary
Path Not Found
\"%@\" query failed!
v8@?0
ERR
Thread %d crashed with Thread State:
Get failure when calling API of libFDR
SIGFPE
SIGALRM
The entry %@ mounted personalized disk image with type %@
kMobileStorageDeviceTypeKey
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_3
The system profiler exited
libZhuGeInternalArmory.dylib
ZhuGeInternalService.xpc
No threads got from task!
Failed to set action for SIGFPE, error %d(%s)!
Unknown class name!
+[NSNumber(ZhuGe) integerFromCInt:size:isSigned:needSwap:]
Please make sure the file exists
Please make sure the correct SE type is input
Failed to dlopen ZhuGe internal armory dylib with error: %s!
\n
ZhuGePrintStderr
getProcInfo
getZhuGeCryptexPathsWithError
Added %s to Cryptex paths array
MGQuery
+[ZhuGeSupportAssistant isKey:withError:]
SIGSTOP
Failed to get ZhuGe armory handler!
Data %@ might be truncated(data size %@, required size %@, maximum supported size %@)
Current XPC connection is not entitled for internal key \"%@\"!
keysDict pointer is nil!
SIGXCPU
In %@, aCache pointer is nil!
Failed to get a shared instance for \"%@\"!
The input data may be unexpected and cannot be processed
-[ZhuGeService isCallerEntitledforInternalKey:withError:]
Failed to set action for SIGSEGV, error %d(%s)!
kMobileStorageMountPathKey
Flexible ZhuGe Key Invalid
Didn't successfully call init related method
The string is not a valid ZhuGe key
Please check the name that being querying
VBIOS Version
No crash thread from context!
SIGBUS
+[ZhuGeSupportAssistant getDylibHandlerWithError:]
Class Type Wrong
Please check sysdiagnose lockdown related log
Sysconfig Key Invalid
arm64
ZhuGe received a relative path
MobileGestalt Not Supported
graphicsArray pointer is nil!
Entitlement Unsupported
Failed to sysctlnametomib(sysctl.proc_cputype), error %d(%s)!
SIGKILL
Path Invalid
-[ZhuGeService setMGKey:getValueAndError:]
ZhuGeService
w
The system profiler report crashed
In bulk query, failed to get internal service proxy for internal keys!
Catch the NULL format pointer from: %s %s(%ld)
Method Invocation Get Failed
Failed to cache entitlement validation result for key \"%@\", error: %@!
Failed to register mach exception handler!
getTaskImageInfo
Failed to read frame from addr(0x%016llx), error %d(%s)!
Unsupported ARM state!
SIGABRT
Entry %@ doesn't contain personalized image type
Unsupported entitlement or the entitlement type
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]
%s ERR: Cannot print serial log!\n
x86
PersonalizedImageType
Encode Failed
Illegal ZhuGe Error Code!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeService/ZhuGeService.m
-[ZhuGeService isCallerEntitledforKey:withError:]
Option ROM Version
/usr/lib/libcryptex.dylib
Please check whether the dylib provided correctly
RegEx Not Matched
key pointer is nil!
Failed to connect \"%@\"!
Failed to lookup mobile storage devices
Device type in entry %@ is not disk image
SP Report Crashed
-[ZhuGeService setKey:andOptions:andPreferences:getValueAndError:]
-[ZhuGeService setBulkInternalMGKeys:getValuesAndError:]
cryptex_copy_list_4MSM
Issue may be due to the underlying error out of ZhuGe
UnderlyingError can only be NSError, NSString, ZHUGE_NULL or nil
armThreadBacktraceWithUnifiedState
ReleaseType
Please check sysdiagnose FDR related log
The key could possibly be a MobileGestalt key, not supported at all
Get failure when calling API of SecCertificate
%@
========== ABORT: timed out when printing crash information ==========
XPC connection is invalid!
LSB
BSDSignalsCrashHandler
Index %@ of ZhuGeErrorCode table got a wrong code %@
v24@?0@8@\"NSError\"16
%02x
Failed to set action for SIGTRAP, error %d(%s)!
Cannot open certain file
Get failure when calling API of AppleMobileFileIntegrity
ZhuGe Key Further Check Needed
This error code should never be reported
%@%@
Successfully registered BSD signal handler.
SIGIO
registerMachExceptionsHandler_block_invoke
Please check whether there is any underlying isse in the encoding API.
User Defaults Domain Not Exists
XPC Service Connect Failed
arm64_32
 
May due to wrong implementation or system problem
Failed to open IO Master port
The system profiler data type is null
Maybe the name for querying is incorrect
Please make sure the Caller has the correct entitlement
OBJC_CLASS_$_ZhuGeLockerInternalArmory
UnknownFunc
========== BEGIN: caught a BSD signal %d(%s) ==================
Name of the call back function doesn't exist in library
Current process is not a XPC service process
isXPCConnectionEntitled
Failed to get ZhuGe internal support path for dylib handler!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeLog.m
EXC_EMULATION
Nothing Wrong
Please check your code to use a correct class
Wrong key or the key is not configured
Type of some object is invalid
Failed to get the dylib shared instance!
com.apple.ZhuGe.ZhuGeCrashReporter.getTaskImageInfo
Maybe the method name is incorrect
Object Length Invalid
\n%@{\n%@Domain   = %@\n%@Code     = %@\n%@UserInfo = {\n%@Description        = %@\n%@FailureReason      = %@\n%@RecoverySuggestion = %@\n%@UnderlyingError    = %@\n%@}
-[ZhuGeService setBulkInternalKeys:getValuesAndError:]
MACH_HEADER
CFPreference API return error
Path or name of XPC service might be incorrect
Connection to \"%@\" interrupted!
%s %@
SIGEMT
Failed to set action for SIGPIPE, error %d(%s)!
cryptexIdentifier pointer is nil!
\x85
SIGXFSZ
Entry %@ doesn't contain a valid personalized disk image path
ZhuGe Error module itself got some issues
Flexible key doesn't macth its pattern
Trying internal MG key \"%@\"
%s ERR: 
/dev/console
setActionForSignals
{%d:0x%llx}
SIGVTALRM
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeUtils.m
cryptex_msm_array_destroy
Call Back Function Not Found
Key Duplicated
One graphic in graphics array does not contain \"sppci_model\"
sysctl.proc_cputype
Failed to get cpu type for pid(%d), error %d(%s)!
SIGQUIT
com.apple.AppleDeviceQueryService
\x83
Probaby the wrong arguments defined in xml
Near Field SE Type Invalid
%s%6s: 0x%016llx
iPhone OS
Failed to link mobile storage framework
Please check the CLI option that input
Failed to call SMC APIs, unsupported SMC key etc.
The caller is not entitled for internal key \"%@\"!
Failed to create crash thread!
SIGUSR2
May due to an invalid IO Service
com.apple.ZhuGeInternalService
SIGILL
SIGCONT
Class type of object is unexpected, usually detected with \"isKindOfClass:\" method
SP Data Report Invalid
SP Exited
Get failure when calling API of Img4
Failed to get Cryptex paths
SIGURG
Failed to query MobileGestalt for \"%@\", MobileGestalt error code %@!
Cannot connect to lockdown daemon via a local socket
SP Data Type Null
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/NSArray+ZhuGe.m
createCrashReport
Failed to allocate for crash_report_thread, error %d(%s)!
Failed to set action for SIGILL, error %d(%s)!
ACE Command Failed
SecCertificate API Failed
SIGWINCH
+[ZhuGeSupportAssistant getDylibHandlerWithError:]_block_invoke
Please file a radar against \"ZhuGe|all\"
Sysctl Failed
Check error description to find out recvoery suggestion
Please make sure the process is using memory reasonably
Method Invoke Failed
Failed to set exception ports for current task, error %d(%s)!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeSupportAssistant.m
Please check path of the code calling CFPreference
Please make sure the way using ZhuGe is correct
Specific Hardware Needed
Failed to get internal service proxy for internal MG key \"%@\"!
SIGTRAP
cryptex_msm_get_string
The path just doesn't exist or the way to find the path is incorrect.
The failure might be expected without specific hardware
Please check the data source or code
SIGSEGV
/System/Library/CoreServices/SystemVersion.plist
Tries All Failed
0x%016llx - 0x%016llx %s %s <%s> %s
getProcCPUType
SIGHUP
kMobileStorageDeviceTypeDiskImage
Check error description to understand failure reason
Unsupported SE Type
Received internal key: \"%@\"
Failed to allocate mach port, error %d(%s)!
Please check the path of IO entry
Device ID
Failed to create exception port!
Failed to dlopen ZhuGe armory dylib with error: %s!
Error System Issue
Please contact Near Field team for issue triaging
SMC Service Failed
Invalid ZhuGe Error Code!
Begin: bulk query keys
Internal XPC connection is already available
catch_mach_exception_raise
FactoryDiskImage
OS Unknown
The property list cannot be serialized
Usually this error code shall not be displayed
Please check newly added code that calling ZhuGeError API
WRN
%-21s%s
EXC_RPC_ALERT
Entry %@ doesn't contain a valid device type
OBJC_CLASS_$_ZhuGeLockerArmory
May due to an invalid IO Service connection
Memory Exhausted
Failed to get configuration for internal key \"%@\"!
No thread specified!
\"%@\" is not a vaild MobileGestalt key!
Options
v24@?0@\"NSDictionary\"8@\"NSError\"16
Skip retrieving internal support path in restoreOS
Translated
MSB
%s\n
Invalid crash thread in report
ZHUGE_NULL
Please check whether the call back function name exists in the library
Please make sure IO Service connection is valid
Lockdown Query Failed
SP Report Creation failed
In bulk query, failed to query internal keys!
Chipset Model
Option of the CLI command is not supported
No SMC service available on this device.
In bulk query, key \"%@\" failed! Error: %@
========== BEGIN: caught a mach exception ============================
getZhuGeFDIPathsWithError
Something might be wrong with Near Field component
[ZhuGe]
EXC_BAD_ACCESS
IO Service Get Failed
EXC_UNSUPPORTED
Bits will be truncated since real size is %@, while required size is %@
Please check whether the key or alias input correct, or implemented.
Unexpected SMC Key Size returned
-[ZhuGeService isCallerEntitledForService]
-[ZhuGeService setBulkMGKeys:getValuesAndError:]
Unnecessary to explicitly register crash reporter in this environment!
SIGINT
Failed to get a proxy for \"%@\"!
Data Convert Failed
AMFI Get Failed
Possible causes like: SMC service failed to be ported; device type doesn't support it... etc.
error p-pointer is nil!
createCrashReportThread
SIGTERM
ZhuGe Key Not Supported
Please make sure locakdown daemon and local sockets work well
String is invalid, like unpaired quotation, bracket etc.
%s (UUID: %s __TEXT + 0x%zX) 
Failed to set action for SIGBUS, error %d(%s)!
Added %@ to FDI paths array
Current OS is not defined
XPC service name may be invalid
XPC Service denied access due to lacking of entitlement
v24@?0{_CSTypeRef=QQ}8
EXC_BAD_INSTRUCTION
Failed to get the internal dylib shared instance!
Begin: bulk query internal keys
End: bulk query internal keys
========== ABORT: timed out when creating symbolicator ===============
SIGPIPE
+[ZhuGeSupportAssistant getSharedInstanceByName:withError:]
So far so good, keep going
Code Max
Begin: bulk query MG keys
Please check sysdiagnose for more clue
Method Signature Get Failed
Please check whether the path of XPC service correct and existing
{\n%@%@\n%@}
Preferences
armThreadBacktraceFromFP
CFPreference Error
SMC Service Unsupported
Please make sure the entitlement is correctly configured
com.apple.private.ZhuGeSupport.CopyValue
Get entitlement validation result for key \"%@\" from cache
The caller is not entitled for key \"%@\"!
Failed to get FDI paths
Connection to \"%@\" invalidated!
Data Convert To Nil
Underlying service may be not ready
XPC Service Not Exist
ZhuGe exception server does not support catch_mach_exception_raise!
Successfully registered mach exception handler.
Check the string in code or input source
End: bulk query MG keys
Thread %d Crashed:
Failed to get ARM thread state, error %d(%s)!
com.apple.private.ZhuGeInternalSupport.CopyValue
Please check whether device supports the service
Img4 API Failed
Please check regEx related code in ZhuGe
XPC Service Not Available
In bulk query, failed to get internal service proxy for internal MG keys!
Failed to get ZhuGe internal support path for xpc proxy!
EXC_GUARD
+[ZhuGeSupportAssistant getXpcProxyWithError:]
Please check whether the path using is correct
Failed to link CoreSymbolication framework, CSSymbolicatorCreateWithTask is unavailable!
EXC_BREAKPOINT
In %@, key \"%@\" got a wrong cache class type \"%@\"!
Pointer Null
The key is not supported by MobileGestalt
No arm thread backtrace frame pointer specified!
Time Out
This special error code is used for ZhuGe configuration analysis
-[ZhuGeService setInternalKey:andOptions:andPreferences:getValueAndError:]
Begin: bulk query internal MG keys
Failed to create non-crash thread!
i
Failed to validate ZhuGe internal service entitlement for queued connection from pid %@!
UnknownFile
No mobile storage device is detected
INF
Invalid pid: %d!
Failed to copy cryptex list, error %d(%s)
Device may not support the service
End: bulk query internal MG keys
ROM Revision
Input may be missing subkey(s), or something wrong with flexible pattern definition
User defaults doesn't support the specific domain
ZhuGeErrorCode %@ exceed maximum
-[ZhuGeService isCallerEntitledForInternalService]
One graphic in graphics array is not a dictionary, ignore it.
Failed to get proxy for \"%@\"!
Failed to create CS symbolicator!
In %@, aKey pointer is nil!
The option passed in is not supported
/usr/local/ZhuGe/ZhuGeInternalSupport
%s <%s %s(%ld)> ERR: 
catch_mach_exception_raise_state_identity
Failed to get arm thread state, error %d(%s)!
SIGCHLD
Path not exists or the string is not a path
The system profiler report failed to be created
%s ERR: Failed to get a restore log proxy!
XPC connection is already available
Object Type Invalid
Failed to cache entitlement validation result for internal key \"%@\", error: %@!
armThreadBacktrace
Restore
IO Property Not Found
IO Service Open Failed
SMC Key Type Wrong
printCrash_block_invoke
Q
Path Not Absolute
Failed to validate ZhuGe service entitlement for current connection from pid %@!
%s%s\n
Failed to get threads for task, error %d(%s)!
SIGTTOU
SIGINFO
Path of IO entry might be wrong
Maybe the method name or signature is incorrect
Permission Denied
Trying MG key \"%@\"
armThreadSetRegisters
registerMachExceptionsHandler_block_invoke_2
%s
No crash context to report!
Checking entry %@
Value
Failed to register BSD signal handler!
EXC_SOFTWARE
zhuge_debug
Failed to encode with proper API
Thread %d:
Failed to link libcryptex.dylib!
ZhuGe only supports absolute path, caller needs to convert relative path by itself
User have no proper access
%s <ZhuGeLog.m %s(%d)> ERR: Catched NULL format pointer from: %s %s(%ld)\n
sysctl.proc_translated
OBJC_CLASS_$_ZhuGeArmory
Dylib Not Available
+[NSArray(ZhuGe) arrayFromShellCommandString:]
+[NSArray(ZhuGe) graphicInfoArrayFromArray:]
Failed to dump registers for crash thread!
Failed to create dispatch source for receiving mach msg sent to exception port!
atm_diagnostic_config
IO Service Close Failed
v16@?0@\"NSNumber\"8
%-21s%s (%s)
OS Version:
printCrash
Failed to get proc path, error %d(%s)!
EXC_CRASH
SIGTSTP
com.apple.ZhuGe.ZhuGeCrashReporter.registerMachExceptionsHandler
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeInternalSupport/ZhuGeInternalSupportAssistant.m
Failed to set action for SIGABRT, error %d(%s)!
Entry %@ doesn't contain a correct personalized image type
Connection(pid %d) is missing entitlement!
Near Field API Failed
Maybe the method itself got some issue
Please check sysconfig key name input
Didn't successfully get data due to lacking of specific hardware
No crash thread in report
EXC_RESOURCE
IODeviceTree:/options
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/NSNumber+ZhuGe.m
This failure is intentionally, please check the input data length, content etc.
Lockdown Connect Failed
Get entitlement validation result for internal key \"%@\" from cache
-[ZhuGeService setBulkKeys:getValuesAndError:]
SMC key information indicate a wrong type
%s (%s)
The key is not a ZhuGe native key
The caller failed entitlement check!
End: bulk query keys
Path:
keysList pointer is nil!
Didn't find ZhuGe internal Support Path
Failed to get ARM thread exception state, error %d(%s)!
iCEIK
v16@?0@\"NSError\"8
/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib
SMC Key Size Unexpected
Caller's entitlement value is mismatched with required one
SIGTTIN
SIGUSR1
Key Not Found
String Format Wrong
In %@, error p-pointer is nil!
Decode Failed
SMC Key Name Invalid
In bulk query, failed to query internal MG keys!
com.apple.FactoryCryptexSupport
Please make sure the key being querying correct
Please make sure the option is correct
Reserved ZhuGeErrorCode %@ shall not be the argument
ENTITLEMENT
In bulk query, MG Key \"%@\" failed! Error: %@
arm
Failed to dispatch MIG mach exception server!
MobileStorageCopyDevicesWithError
Required size is %@, while usually it should be %@ or %@ or %@ or %@
Please check whether the user has the privilege
Please make sure the domain is correctly inputted
Please check latest code that using ZhuGe error API
Failed to validate ZhuGe internal service entitlement for current connection from pid %@!
ZhuGe internal support path is updated to: %@
com.apple.zhuge
Please make sure IO Service is valid
All possible tries has failed
ZhuGe Key Not Native Supported
VRAM Size
Failed to allocate crash report, error %d(%s)!
Native
__TEXT
Option Unsupported
Failed to validate ZhuGe service entitlement for queued connection from pid %@!
Failed to get configuration for key \"%@\"!
Error
Failed to get os version, error %d(%s)!
-[ZhuGeCache setCache:forKey:withError:]
May due to an invalid IO entry
XPC Service Entitlement Missing
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_3
registerMachExceptionsHandler
ZhuGeRestoreLogProtocol
ZhuGeService
ZhuGe
ZhuGeInternalServiceProtocol
ZhuGeSingletonService
ZhuGeLockerService
ZhuGeCache
ServiceDelegate
NSXPCListenerDelegate
NSObject
ZhuGeInternalSupportAssistant
ZhuGeServiceProtocol
ZhuGeSupportAssistant
ZhuGeDescription
T@\"NSString\",?,R,C
fileExistsAtPath:isDirectory:
firstObject
performSelector:
setAllXpcConnections:
stringByReplacingOccurrencesOfString:withString:
numberWithLong:
_cacheDict
characterSetWithCharactersInString:
classList
getXpcProxyWithError:
macAddressStringFromData:
numberWithUnsignedInteger:
setKey:andOptions:andPreferences:getValueAndError:
delCacheForKey:
T@\"NSString\",R,V_armoryClassName
_cacheList
domainString
macAddressStringFromSysconfigDataSixByte:
mutableBytes
scanInt:
containsObject:
numberWithChar:
serviceListener
T@\"NSString\",R,V_domainString
capacity
initWithName:andCapacity:andCacheType:
scannerWithString:
setBulkInternalKeys:getValuesAndError:
appendBytes:length:
performSelector:withObject:
scanHexInt:
setXpcConnection:
boolFromData:needNegate:
dylibHandler
hash
isKey:withError:
numberWithUnsignedChar:
userInfo
T^v
domain
initWithData:encoding:
setAreXpcConnectionsChecked:
setRemoteObjectInterface:
T@\"NSMutableArray\",&,V_allXpcConnections
T@\"NSMutableArray\",R,V_cacheList
T@\"NSXPCConnection\",&,V_xpcConnection
TB
addObject:
executeCacheRefresh
integerValue
replaceObjectAtIndex:withObject:
baseEntitlement
_ZhuGeDescriptionWithLayer:
cacheType
descriptionFromZhuGeErrorCode:
hexStringFromData:
setInvalidationHandler:
stringByPaddingToLength:withString:startingAtIndex:
stringWithFormat:
aRecursiveMutex
_baseEntitlement
clearCache
debugDescription
initWithFormat:arguments:
isCallerEntitledforKey:withError:
numberWithInteger:
performSelector:withObject:withObject:
setWithObjects:
initWithCapacity:
lastPathComponent
listener:shouldAcceptNewConnection:
xpcConnection
zone
boolValue
cacheList
retain
stringByTrimmingCharactersInSet:
getBytes:range:
description
initWithBytes:length:encoding:
isXpcConnectionValid
numberWithLongLong:
numberWithUnsignedLong:
substringWithRange:
numberWithUnsignedInt:
remoteObjectInterface
setBulkKeys:getValuesAndError:
stringByTrimmingCharactersInString:
stringByRightTrimmingCharacter:
_name
_supportAssistantClass
_xpcConnection
arrayWithObjects:count:
isDataConvertibleToVisibleString:
isInternalAssistant
isMemberOfClass:
activate
cStringUsingEncoding:
numberWithShort:
printRemoteLog:withReply:
registerCacheRefresh:
removeObjectAtIndex:
removeObjectForKey:
setBulkMGKeys:getValuesAndError:
T@\"NSNumber\",R,V_capacity
bytes
intValue
invalidate
pathWithComponents:
setClasses:forSelector:argumentIndex:ofReply:
setExportedObject:
setInternalMGKey:getValueAndError:
T@\"NSString\",R,V_name
_areXpcConnectionsChecked
appendFormat:
conformsToProtocol:
hasSuffix:
isEqualToString:
length
name
arrayWithArray:
defaultManager
objectForKey:
recursiveMutex
respondsToSelector:
retainCount
setExportedInterface:
supportAssistantClass
_armoryClassName
_cacheType
T#,R
.cxx_destruct
T@\"NSMutableArray\",&,V_areXpcConnectionsChecked
T@\"NSMutableDictionary\",R,V_cacheDict
stringFromData:
setIsXpcConnectionValid:
accessInstanceVariablesDirectly
recursiveMutexForXpcConnections
dictionaryWithObjects:forKeys:count:
queryKey:andOptions:andPreferences:withError:
setCache:forKey:withError:
setDylibHandler:
sharedInstance
substringToIndex:
T#,R,V_cacheType
initData
isKindOfClass:
numberWithInt:
setBulkInternalMGKeys:getValuesAndError:
setCacheList:
setObject:forKeyedSubscript:
T@\"NSString\",R,C
armoryClassName
T@\"NSMutableArray\",&
characterAtIndex:
initWithServiceName:
interfaceWithProtocol:
isCallerEntitledforInternalKey:withError:
visibleStringFromData:
getCacheForKey:
release
allXpcConnections
getDylibHandlerWithError:
getSharedInstanceByName:withError:
stringWithUTF8String:
TQ,R
_capacity
code
count
dataFromHexString:
integerFromCInt:size:isSigned:needSwap:
removeAllObjects
removeObject:
T#,R,V_supportAssistantClass
T@\"NSString\",R,V_baseEntitlement
getInternalSupportPath
graphicInfoArrayFromArray:
helper
init
isCallerEntitledForInternalService
isCallerEntitledForService
dataWithLength:
_allXpcConnections
arrayFromShellCommandString:
errorWithDomain:code:userInfo:
objectForKeyedSubscript:
processIdentifier
setInterruptionHandler:
synchronousRemoteObjectProxyWithErrorHandler:
isProxy
numberWithBool:
T@\"NSXPCConnection\",&
areXpcConnectionsChecked
countByEnumeratingWithState:objects:count:
substringFromIndex:
valueForEntitlement:
isAtEnd
autorelease
isEqual:
numberWithUnsignedShort:
self
setDelegate:
UTF8String
_domainString
class
getConfigOfKey:withError:
integerFromData:size:truncate:isSigned:needSwap:
objectAtIndex:
stringByLeftTrimmingCharacter:
stringByRemovingCharactersInString:
cacheDict
dictionaryWithContentsOfFile:
numberWithUnsignedLongLong:
superclass
ccccValue
errorWithZhuGeErrorCode:underlyingError:
setInternalKey:andOptions:andPreferences:getValueAndError:
setMGKey:getValueAndError:
@\"NSNumber\"
v48@0:8@16@24@32@?40
v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24
v16@0:8
{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}
B40@0:8@16@24^@32
#16@0:8
v24@0:8@16
B16@0:8
@20@0:8c16
v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24
@24@0:8:16
B24@0:8:16
B32@0:8@16@24
@40@0:8Q16Q24B32B36
@\"NSMutableDictionary\"
Q16@0:8
^{_NSZone=}16@0:8
@\"NSString\"16@0:8
@24@0:8Q16
v32@0:8@16@?24
@16@0:8
@\"NSString\"
#
@32@0:8:16@24
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
@24@0:8@16
@24@0:8^@16
@\"NSXPCConnection\"
@32@0:8@16^@24
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
v24@0:8^v16
B24@0:8@16
@40@0:8@16@24#32
v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
@40@0:8:16@24@32
Vv16@0:8
@48@0:8@16Q24q32B40B44
^{_opaque_pthread_mutex_t=q[56c]}16@0:8
^v16@0:8
@\"NSMutableArray\"
B24@0:8#16
@28@0:8@16B24
@32@0:8Q16@24
v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40
v20@0:8B16
^v24@0:8^@16
B24@0:8@\"Protocol\"16
%{public}@
```
