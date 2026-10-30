# `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`

From the upgrade restore ramdisk (141-29011-104.dmg). 194,784 bytes.

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
@\"NSXPCConnection\"
@28@0:8@16B24
@24@0:8Q16
@32@0:8Q16@24
^{_opaque_pthread_mutex_t=q[56c]}16@0:8
B24@0:8@16
@24@0:8:16
@32@0:8:16@24
@40@0:8:16@24@32
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
@\"NSMutableArray\"
@40@0:8@16@24#32
@\"NSString\"16@0:8
@\"NSNumber\"
@32@0:8@16^@24
v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24
Vv16@0:8
Q16@0:8
B24@0:8@\"Protocol\"16
@40@0:8Q16Q24B32B36
B16@0:8
#16@0:8
@\"NSMutableDictionary\"
@24@0:8@16
v48@0:8@16@24@32@?40
v24@0:8^v16
v16@0:8
@24@0:8^@16
{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}
^v16@0:8
@16@0:8
v20@0:8B16
^v24@0:8^@16
B40@0:8@16@24^@32
#
@48@0:8@16Q24q32B40B44
v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24
v24@0:8@16
@\"NSString\"
v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
B24@0:8#16
B24@0:8:16
^{_NSZone=}16@0:8
B32@0:8@16@24
v32@0:8@16@?24
v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
@20@0:8c16
%{public}@
softlink:r:path:/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage
SIGPIPE
%@ failed to provide a proxy with error : %@!
MGkey pointer is nil!
Failed to query MobileGestalt for \"%@\", MobileGestalt error code %@!
Lockdown Connect Failed
ZhuGe only supports absolute path, caller needs to convert relative path by itself
Please check regEx related code in ZhuGe
The failure might be expected without specific hardware
Device ID
ZhuGePrintStderr
EXC_CRASH
SIGINFO
The system profiler report crashed
EXC_BAD_INSTRUCTION
Failed to dispatch MIG mach exception server!
Maybe the method name is incorrect
Possible causes like: SMC service failed to be ported; device type doesn't support it... etc.
Please make sure the key string is correct
INF
SIGCONT
registerMachExceptionsHandler_block_invoke_2
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCache.m
OBJC_CLASS_$_ZhuGeArmory
Key Duplicated
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeService/ZhuGeService.m
Get entitlement validation result for key \"%@\" from cache
========== ABORT: set signals action failed ========================
Failed to set action for SIGTRAP, error %d(%s)!
Failed to set action for SIGBUS, error %d(%s)!
Underlying service may be not ready
Please check latest code that using ZhuGe error API
/usr/local/ZhuGe/ZhuGeInternalSupport
com.apple.FactoryCryptexSupport
%02x
No crash thread in report
createCrashReport
AMFI Get Failed
Failed to allocate mach port, error %d(%s)!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/NSNumber+ZhuGe.m
Initialization Failed
All possible tries has failed
Code Max
keysDict pointer is nil!
Failed to connect \"%@\"!
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_2
In %@, error p-pointer is nil!
ZhuGe Key Further Check Needed
Failed to get Cryptex paths
w
Code Type:
SIGSYS
Failed to set action for SIGPIPE, error %d(%s)!
The entry %@ mounted personalized disk image with type %@
+[ZhuGeSupportAssistant getDylibHandlerWithError:]
The property list cannot be serialized
kern.osversion
SIGIO
SIGKILL
The system profiler exited
Entitlement Unsupported
Failed to get internal service proxy for internal key \"%@\"!
com.apple.ZhuGeInternalService
ERR
catch_mach_exception_raise
========== END: caught a mach exception ==============================
Entry %@ doesn't contain a valid personalized image type
OBJC_CLASS_$_ZhuGeInternalArmory
(null)
sysctl.proc_translated
Failed to link libcryptex.dylib!
Invalid ZhuGe Error Code!
Failed to get arm thread state, error %d(%s)!
Wrong key or the key is not configured
In bulk query, key \"%@\" failed! Error: %@
Begin: bulk query internal MG keys
Failed to get FDI paths
EXC_GUARD
Failed to lookup mobile storage devices
\"%@\" is not a vaild MobileGestalt key!
This failure is intentionally, please check the input data length, content etc.
No crash context to report!
String Format Wrong
Get failure when calling API of Img4
========== End: caught a BSD signal %d(%s) ==================
Please check whether there is any underlying isse in the decoding API.
IO Service Open Failed
Near Field SE Type Invalid
The key could possibly be a MobileGestalt key, not supported at all
UnknownFile
%-21s%s [%d]
SIGSTOP
Failed to set action for SIGABRT, error %d(%s)!
Error System Issue
Entitlement Mismatched
Get failure when calling API of SecCertificate
%s %@
printCrash_block_invoke
Failed to insert send right for expcetion port, error %d(%s)!
Failed to set action for SIGILL, error %d(%s)!
isXPCConnectionEntitled
Q
cryptex_msm_array_destroy
ACE Command Failed
error p-pointer is nil!
Exception Type:
ZHUGE_NULL
Key of dictionary is redundant
com.apple.ZhuGe.ZhuGeCrashReporter.registerMachExceptionsHandler
ZhuGe Key Not Supported
Class Type Wrong
Didn't successfully call init related method
No SMC service available on this device.
catch_mach_exception_raise_state_identity
Failed to link CoreSymbolication framework, CSSymbolicatorCreateWithTask is unavailable!
getZhuGeFDIPathsWithError
ZhuGe Error module itself got some issues
SP Data Report Invalid
SP Exited
MSB
-[ZhuGeService setBulkInternalKeys:getValuesAndError:]
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCrashReporter.m
getTaskImageInfo
Unsupported ARM thread state!
Input may be missing subkey(s), or something wrong with flexible pattern definition
In bulk query, failed to get internal service proxy for internal keys!
-[ZhuGeService setBulkMGKeys:getValuesAndError:]
%@
Failed to register BSD signal handler!
In %@, aKey pointer is nil!
Didn't find the expected path
String is invalid, like unpaired quotation, bracket etc.
Operation is not done in certain time
%s: 
No threads got from task!
Failed to get ARM thread exception state, error %d(%s)!
atm_diagnostic_config
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeSupportAssistant.m
IO Property Not Found
Lockdown Query Failed
The system profiler report failed to be created
Internal XPC connection is already available
armThreadBacktraceWithUnifiedState
SIGTTIN
+[ZhuGeSupportAssistant getDylibHandlerWithError:]_block_invoke
\n%@{\n%@Domain   = %@\n%@Code     = %@\n%@UserInfo = {\n%@Description        = %@\n%@FailureReason      = %@\n%@RecoverySuggestion = %@\n%@UnderlyingError    = %@\n%@}
-[ZhuGeService isCallerEntitledForInternalService]
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeInternalSupport/ZhuGeInternalSupportAssistant.m
Some internal issues happened when converting data
Quotation \"%c\" is not paired in command \"%@\"!
OBJC_CLASS_$_ZhuGeLockerInternalArmory
May due to wrong implementation or system problem
Permission Denied
Please make sure the entitlement is correctly configured
Failed to dlopen ZhuGe internal armory dylib with error: %s!
/dev/console
Unsupported ARM state!
IODeviceTree:/options
kMobileStorageMountPathKey
Please check sysdiagnose FDR related log
Object Length Invalid
SMC key information indicate a wrong type
/usr/lib/libcryptex.dylib
kMobileStorageDeviceTypeKey
+[ZhuGeSupportAssistant isKey:withError:]
Please make sure the file exists
SP Data Type Null
sppci_model
Check error description to find out recvoery suggestion
Please check path of the code calling CFPreference
Failed to get proxy for \"%@\"!
ZhuGeLog
\x83
Pointer Null
Img4 API Failed
Please check newly added code that calling ZhuGeError API
Reserved ZhuGeErrorCode %@ shall not be the argument
No thread specified!
registerMachExceptionsHandler_block_invoke
+[ZhuGeSupportAssistant getSharedInstanceByName:withError:]
Received internal key: \"%@\"
Invalid crash thread in report
x86_64
Entry %@ doesn't contain a valid personalized disk image path
Maybe unsupported lockdown domain, key or maybe some underlying issue in lockdown daemon
Method Invocation Get Failed
Path Invalid
Sysconfig Key Invalid
Please check the data source or code
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]
ZhuGeService
Invalid pid: %d!
Failed to get cpu type for pid(%d), error %d(%s)!
SIGFPE
In %@, aCache pointer is nil!
Path Not Found
Current XPC connection is not entitled for internal key \"%@\"!
\n
 
Please check your code to use a correct class
Cannot open certain file
Please check the name that being querying
Failed to validate ZhuGe internal service entitlement for queued connection from pid %@!
:
Failed to allocate for crash_report_thread, error %d(%s)!
Failed to destruct exception port!
\"%@\" query failed!
Connection to \"%@\" interrupted!
Thread %d Crashed:
x86
PersonalizedImageType
Please make sure locakdown daemon and local sockets work well
Please check whether the path using is correct
The caller is not entitled for key \"%@\"!
SIGQUIT
Please check the path of IO entry
%-21s%s (%s)
SIGCHLD
Type of some object is invalid
Option Unsupported
Received key: \"%@\"
arm64_32
MobileStorageCopyDevicesWithError
SMC Key Type Wrong
Value Out Of Range
ZhuGe service connected for current connection from pid %@
ZhuGe internal support path is updated to: %@
SIGUSR1
BSDSignalsCrashHandler
Data Convert To Nil
SMC Key Size Unexpected
Please check whether the path of XPC service correct and existing
???
v24@?0{_CSTypeRef=QQ}8
cryptex_msm_get_string
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_2
The key is not supported by MobileGestalt
com.apple.private.ZhuGeInternalSupport.CopyValue
-[ZhuGeService setBulkInternalMGKeys:getValuesAndError:]
End: bulk query internal MG keys
%s ERR: Restore log connection error: %@
catch_mach_exception_raise_state
EXC_UNSUPPORTED
JSON String Invalid
ZhuGe received a relative path
cryptex_copy_list_4MSM
v24@?0@\"NSDictionary\"8@\"NSError\"16
Trying MG key \"%@\"
<%@ %@(%@)>
Name of the call back function doesn't exist in library
Encode Failed
Maybe the name for querying is incorrect
%-21s%s
EXC_EMULATION
getZhuGeCryptexPathsWithError
No arm thread backtrace frame pointer specified!
Please check the CLI option that input
Data Convert Failed
Please make sure the process is using memory reasonably
-[ZhuGeService isCallerEntitledforInternalKey:withError:]
The data indexed by the indexArray is not valid
========== BEGIN: caught a mach exception ============================
Failed to create exception port!
Failed to set action for SIGFPE, error %d(%s)!
/usr/local/lib/libcryptex.dylib
Please check sysdiagnose for more clue
MobileGestalt Not Supported
FactoryDiskImage
Path of IO entry might be wrong
iCEK
-[ZhuGeService isCallerEntitledforKey:withError:]
%s (UUID: %s __TEXT + 0x%zX) 
Chipset Model
SIGBUS
Added %s to Cryptex paths array
Failed to open IO Master port
This error code should never be reported
ZhuGeErrorCode %@ exceed maximum
keysList pointer is nil!
libZhuGeInternalArmory.dylib
registerCrashReporter
Please file a radar against \"ZhuGe|all\"
Path or name of XPC service might be incorrect
Get entitlement validation result for internal key \"%@\" from cache
SIGILL
Check error description to understand failure reason
Please check whether device supports the service
Dylib Not Available
Key Not Found
Name of queried sysconfig key might be wrong
Please make sure the option is correct
-[ZhuGeService setInternalKey:andOptions:andPreferences:getValueAndError:]
%s%6s: 0x%016llx
Failed to read frame from addr(0x%016llx), error %d(%s)!
Failed to set exception ports for current task, error %d(%s)!
Begin: bulk query MG keys
Failed to create dispatch source for receiving mach msg sent to exception port!
CFPreference Error
Please check whether there is any underlying isse in the encoding API.
Flexible key doesn't macth its pattern
Please make sure the correct SE type is input
========== ABORT: timed out when printing crash information ==========
Failed to create non-crash thread!
Please check whether the user has the privilege
User Defaults Domain Not Exists
v16@?0@\"NSError\"8
SIGWINCH
Please make sure the Caller has the correct entitlement
Current XPC connection is not entitled for key \"%@\"!
Connection to \"%@\" invalidated!
getProcInfo
SIGXCPU
The string is not a valid ZhuGe key
Please check sysdiagnose lockdown related log
Please make sure the domain is correctly inputted
The caller is not entitled for internal key \"%@\"!
Successfully registered BSD signal handler.
Path:
zhuge_debug
ZhuGeInternalService.xpc
[ZhuGe]
OS Version:
Didn't successfully get data due to lacking of specific hardware
ZhuGe service bridge-connected for current connection from pid %@
Preferences
com.apple.ZhuGe.ZhuGeCrashReporter.printCrash
Please check whether the call back function name exists in the library
Cannot connect to lockdown daemon via a local socket
Value
In bulk query, query key: \"%@\" from %@entrusted MG
SIGHUP
In %@, key \"%@\" got a wrong cache class type \"%@\"!
Please check whether the key or alias input correct, or implemented.
Begin: bulk query keys
VBIOS Version
Failed to get backtrace symbols!
SIGINT
Failed to get a proxy for \"%@\"!
Please make sure IO Service connection is valid
Specific function isn't supported in current OS or environment.
User have no proper access
The caller failed entitlement check!
EXC_BAD_ACCESS
SIGTSTP
XPC connection is invalid!
May due to an invalid IO Service
Maybe the method itself got some issue
Some pointer shall not be NULL
com.apple.private.ZhuGeSupport.CopyValue
v8@?0
May due to an invalid IO entry
The path just doesn't exist or the way to find the path is incorrect.
User defaults doesn't support the specific domain
Get failure when calling API of AppleMobileFileIntegrity
/System/Library/CoreServices/SystemVersion.plist
Pattern string can not cover the case
SP Report Creation failed
Failed to validate ZhuGe service entitlement for current connection from pid %@!
ZhuGe exception server does not support catch_mach_exception_raise_state!
Failed to get ZhuGe armory handler!
In bulk query, failed to get internal service proxy for internal MG keys!
Catch the NULL format pointer from: %s %s(%ld)
Process:
SIGEMT
Memory is not enough
XPC Service denied access due to lacking of entitlement
EXC_SOFTWARE
SIGXFSZ
kMobileStorageDeviceTypeDiskImage
+[NSNumber(ZhuGe) integerFromData:size:truncate:isSigned:needSwap:]
Call Back Function Not Found
Current OS is not defined
Sysctl Failed
v16@?0@\"NSNumber\"8
Failed to dump registers for crash thread!
Unsupported SE Type
iPhone OS
EXC_RPC_ALERT
setActionForSignals
Failed to have shared instance for \"%@\"!
RegEx Not Matched
Time Out
Unsupported entitlement or the entitlement type
Failed to cache entitlement validation result for key \"%@\", error: %@!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeLog.m
com.apple.zhuge
Class type of object is unexpected, usually detected with \"isKindOfClass:\" method
Failed to get the internal dylib shared instance!
In bulk query, query key: \"%@\" in %@entrusted way
%s
Thread %d:
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_4
File Open Failed
Object Type Invalid
PropertyList Serialization Failed
UnderlyingError can only be NSError, NSString, ZHUGE_NULL or nil
key pointer is nil!
Option ROM Version
{%d:0x%llx}
Failed to get proc path, error %d(%s)!
The key is not a ZhuGe native key
-[ZhuGeCache setCache:forKey:withError:]
SMC Key Name Invalid
ROM Revision
printCrash
EXC_RESOURCE
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeUtils.m
MGQuery
OBJC_CLASS_$_ZhuGeLockerArmory
+[NSNumber(ZhuGe) integerFromCInt:size:isSigned:needSwap:]
%s ERR: Failed to get a restore log proxy!
The input data may be unexpected and cannot be processed
Please check whether the dylib provided correctly
Failed to create IORegistryEntry iterator
Usually this error code shall not be displayed
VRAM Size
Binary Images:
0x%016llx - 0x%016llx %s %s <%s> %s
Failed to get ARM thread state, error %d(%s)!
Please make sure the key being querying correct
Failed to get configuration for key \"%@\"!
__TEXT
Something might be wrong with Near Field component
-restore
CFPreference API return error
XPC Service Connect Failed
Failed to get internal service proxy for internal MG key \"%@\"!
armThreadBacktrace
Required size is %@, while usually it should be %@ or %@ or %@ or %@
Tries All Failed
EXC_ARITHMETIC
Flexible ZhuGe Key Invalid
graphicsArray pointer is nil!
SIGPROF
registerMachExceptionsHandler
/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib
Unknown class name!
Path Not Absolute
Entry %@ is not a dictionary
Caller's entitlement value is mismatched with required one
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke_3
WRN
Bits will be truncated since real size is %@, while required size is %@
Option or input value is not in defined range
End: bulk query keys
Failed to get proc info, error %d(%s)!
arm64
Failed to copy cryptex list, error %d(%s)
Device type in entry %@ is not disk image
Nothing Wrong
Memory Exhausted
Failed to validate ZhuGe service entitlement for queued connection from pid %@!
SIGTERM
========== BEGIN: caught a BSD signal %d(%s) ==================
Failed to link mobile storage framework
Issue Underlying
Please check if you really want to try this function in current OS or environment
Please check sysdiagnose for more detail
Failed to get configuration for internal key \"%@\"!
Skip retrieving internal support path in restoreOS
LSB
OS Unknown
XPC Service Not Exist
%@%@
========== ABORT: timed out when creating symbolicator ===============
Failed to set action for SIGSEGV, error %d(%s)!
Entry %@ doesn't contain a valid device type
Near Field API Failed
We may need to check with libSMC together
Please check sysconfig key name input
-[ZhuGeService setKey:andOptions:andPreferences:getValueAndError:]
One graphic in graphics array is not a dictionary, ignore it.
%s%s\n
No crash thread from context!
%s (%s)
So far so good, keep going
Failed to sysctlnametomib(sysctl.proc_cputype), error %d(%s)!
createExceptionPort
May due to an invalid IO Service connection
ENTITLEMENT
Failed to find class symbol for \"%@\" with error: %s!
FDR API Failed
SMC Service Unsupported
XPC Service Not Available
SecCertificate API Failed
iCEIK
In bulk query, MG Key \"%@\" failed! Error: %@
sysctl.proc_cputype
Native
com.apple.ZhuGe.ZhuGeCrashReporter.getTaskImageInfo
MACH_HEADER
IO Service Get Failed
-[ZhuGeService setBulkKeys:getValuesAndError:]
Thread %d crashed with Thread State:
Issue may be due to the underlying error out of ZhuGe
Device may not support the service
OS Unsupported
Begin: bulk query internal keys
+[ZhuGeInternalSupportAssistant getInternalSupportPath]
%s <ZhuGeLog.m %s(%d)> ERR: Catched NULL format pointer from: %s %s(%ld)\n
Failed to create crash thread!
Failed to encode with proper API
Get failure when calling API of libFDR
Check the string in code or input source
Didn't find ZhuGe internal Support Path
%s <%s %s(%ld)> ERR: 
Failed to dlopen ZhuGe armory dylib with error: %s!
Option of the CLI command is not supported
Method Invoke Failed
One graphic in graphics array does not contain \"sppci_model\"
Failed to get a shared instance for \"%@\"!
Probaby the wrong arguments defined in xml
Length of some object is unexpected
Unnecessary to explicitly register crash reporter in this environment!
armThreadSetRegisters
Entry %@ doesn't contain a correct personalized image type
Data %@ might be truncated(data size %@, required size %@, maximum supported size %@)
Illegal ZhuGe Error Code!
Error
In bulk query, failed to query internal MG keys!
Failed to create CS symbolicator!
Current process is not a XPC service process
UnknownFunc
Failed to get os version, error %d(%s)!
Maybe the method name or signature is incorrect
Specific Hardware Needed
-[ZhuGeService isCallerEntitledForService]
Options
%s ERR: Cannot print serial log!\n
ZhuGe exception server does not support catch_mach_exception_raise!
armThreadBacktraceFromFP
Index %@ of ZhuGeErrorCode table got a wrong code %@
End: bulk query internal keys
Failed to get ZhuGe internal support path for xpc proxy!
ReleaseType
Error Customized
IO Service Mismatching
Connection(pid %d) is missing entitlement!
\x85
Path not exists or the string is not a path
Translated
+[ZhuGeSupportAssistant getXpcProxyWithError:]_block_invoke_3
Decode Failed
%s ERR: 
SIGVTALRM
i
Added %@ to FDI paths array
SP Report Crashed
SIGTRAP
com.apple.AppleDeviceQueryService
Checking entry %@
XPC connection is already available
The ACE command returns an error
The option passed in is not supported
SIGABRT
SIGURG
CLI Option Unsupported
Failed to decode with proper API
The system profiler data type is null
-[ZhuGeService setInternalMGKey:getValueAndError:]
Failed to get the dylib shared instance!
/Library/Caches/com.apple.xbs/C31D3C13-6EAA-4437-88E2-0A7E4FB26D1F/TemporaryDirectory.0yNvns/Sources/ZhuGe_Service/ZhuGeCommon/NSArray+ZhuGe.m
+[ZhuGeSupportAssistant getXpcProxyWithError:]
Failed to call SMC APIs, unsupported SMC key etc.
This special error code is used for ZhuGe configuration analysis
v24@?0@8@\"NSError\"16
+[NSArray(ZhuGe) graphicInfoArrayFromArray:]
Failed to get threads for task, error %d(%s)!
arm
Restore
Entry %@ doesn't contain personalized image type
Method Signature Get Failed
SMC Service Failed
Trying internal MG key \"%@\"
Failed to allocate crash report, error %d(%s)!
SIGUSR2
ZhuGe is running well
IO Entry Not Found
Unexpected SMC Key Size returned
ZhuGe Key Not Native Supported
XPC Service Entitlement Missing
+[ZhuGeInternalSupportAssistant getDylibHandlerWithError:]
SIGTTOU
Please make sure the way using ZhuGe is correct
XPC service name may be invalid
Failed to cache entitlement validation result for internal key \"%@\", error: %@!
IO Service Close Failed
-[ZhuGeService setMGKey:getValueAndError:]
Retrieving unchanged internal supported path: %@
getProcCPUType
createCrashReportThread
Please make sure IO Service is valid
Please contact Near Field team for issue triaging
Failed to validate ZhuGe internal service entitlement for current connection from pid %@!
Failed to get ZhuGe internal support path for dylib handler!
Failed to register mach exception handler!
SIGSEGV
SIGALRM
The dylib does not exists or too old version
{\n%@%@\n%@}
No mobile storage device is detected
+[NSArray(ZhuGe) arrayFromShellCommandString:]
+[ZhuGeInternalSupportAssistant getXpcProxyWithError:]_block_invoke
Successfully registered mach exception handler.
cryptexIdentifier pointer is nil!
In bulk query, failed to query internal keys!
End: bulk query MG keys
%s\n
EXC_BREAKPOINT
ZhuGeRestoreLogProtocol
ServiceDelegate
ZhuGeInternalSupportAssistant
ZhuGeLockerService
ZhuGeServiceProtocol
NSXPCListenerDelegate
NSObject
ZhuGeService
ZhuGe
ZhuGeInternalServiceProtocol
ZhuGeSingletonService
ZhuGeCache
ZhuGeSupportAssistant
aRecursiveMutex
activate
appendFormat:
code
getSharedInstanceByName:withError:
numberWithUnsignedChar:
queryKey:andOptions:andPreferences:withError:
serviceListener
_ZhuGeDescriptionWithLayer:
autorelease
debugDescription
isEqual:
lastPathComponent
length
numberWithShort:
_cacheList
addObject:
isDataConvertibleToVisibleString:
macAddressStringFromData:
objectAtIndex:
replaceObjectAtIndex:withObject:
setClasses:forSelector:argumentIndex:ofReply:
setKey:andOptions:andPreferences:getValueAndError:
numberWithChar:
_areXpcConnectionsChecked
ccccValue
initWithFormat:arguments:
isCallerEntitledforInternalKey:withError:
removeObject:
removeObjectAtIndex:
setBulkKeys:getValuesAndError:
T@\"NSMutableArray\",&,V_allXpcConnections
arrayFromShellCommandString:
bytes
cacheList
descriptionFromZhuGeErrorCode:
domainString
initWithData:encoding:
integerValue
T@\"NSString\",R,V_armoryClassName
arrayWithObjects:count:
initData
isCallerEntitledForService
performSelector:withObject:withObject:
setAreXpcConnectionsChecked:
setObject:forKeyedSubscript:
setXpcConnection:
dylibHandler
graphicInfoArrayFromArray:
printRemoteLog:withReply:
retain
scanInt:
setBulkMGKeys:getValuesAndError:
setInvalidationHandler:
sharedInstance
stringByRightTrimmingCharacter:
count
defaultManager
description
firstObject
invalidate
numberWithUnsignedInt:
setBulkInternalKeys:getValuesAndError:
getCacheForKey:
T@\"NSString\",?,R,C
_baseEntitlement
characterAtIndex:
numberWithInt:
valueForEntitlement:
numberWithLong:
_cacheType
cStringUsingEncoding:
errorWithDomain:code:userInfo:
hexStringFromData:
isXpcConnectionValid
stringByLeftTrimmingCharacter:
stringByPaddingToLength:withString:startingAtIndex:
arrayWithArray:
T@\"NSMutableArray\",&
boolValue
getInternalSupportPath
numberWithInteger:
setIsXpcConnectionValid:
setMGKey:getValueAndError:
substringWithRange:
numberWithBool:
getConfigOfKey:withError:
mutableBytes
performSelector:withObject:
scanHexInt:
setRemoteObjectInterface:
stringByRemovingCharactersInString:
stringWithFormat:
baseEntitlement
_armoryClassName
characterSetWithCharactersInString:
stringByReplacingOccurrencesOfString:withString:
superclass
visibleStringFromData:
isProxy
armoryClassName
UTF8String
_allXpcConnections
conformsToProtocol:
initWithCapacity:
stringWithUTF8String:
substringToIndex:
T@\"NSMutableDictionary\",R,V_cacheDict
T@\"NSString\",R,V_domainString
TB
cacheDict
isCallerEntitledForInternalService
performSelector:
self
setInternalMGKey:getValueAndError:
TQ,R
helper
isKey:withError:
macAddressStringFromSysconfigDataSixByte:
recursiveMutex
removeObjectForKey:
setInternalKey:andOptions:andPreferences:getValueAndError:
userInfo
T@\"NSString\",R,V_baseEntitlement
dataFromHexString:
domain
isMemberOfClass:
setExportedObject:
containsObject:
T@\"NSString\",R,C
_cacheDict
appendBytes:length:
executeCacheRefresh
initWithServiceName:
numberWithLongLong:
objectForKeyedSubscript:
T#,R,V_supportAssistantClass
delCacheForKey:
setWithObjects:
fileExistsAtPath:isDirectory:
isAtEnd
areXpcConnectionsChecked
init
retainCount
scannerWithString:
setCacheList:
T@\"NSMutableArray\",R,V_cacheList
boolFromData:needNegate:
dictionaryWithContentsOfFile:
interfaceWithProtocol:
isInternalAssistant
objectForKey:
setInterruptionHandler:
_supportAssistantClass
T#,R
release
capacity
setDelegate:
setExportedInterface:
T@\"NSString\",R,V_name
T@\"NSXPCConnection\",&
_xpcConnection
numberWithUnsignedLongLong:
numberWithUnsignedShort:
setAllXpcConnections:
supportAssistantClass
zone
T@\"NSNumber\",R,V_capacity
_name
cacheType
class
errorWithZhuGeErrorCode:underlyingError:
hash
initWithName:andCapacity:andCacheType:
T#,R,V_cacheType
_capacity
integerFromCInt:size:isSigned:needSwap:
setBulkInternalMGKeys:getValuesAndError:
T@\"NSXPCConnection\",&,V_xpcConnection
.cxx_destruct
classList
getXpcProxyWithError:
initWithBytes:length:encoding:
isCallerEntitledforKey:withError:
substringFromIndex:
_domainString
dictionaryWithObjects:forKeys:count:
hasSuffix:
integerFromData:size:truncate:isSigned:needSwap:
numberWithUnsignedInteger:
remoteObjectInterface
setCache:forKey:withError:
ZhuGeDescription
dataWithLength:
getBytes:range:
countByEnumeratingWithState:objects:count:
isKindOfClass:
processIdentifier
T@\"NSMutableArray\",&,V_areXpcConnectionsChecked
isEqualToString:
pathWithComponents:
xpcConnection
stringFromData:
allXpcConnections
intValue
setDylibHandler:
stringByTrimmingCharactersInString:
synchronousRemoteObjectProxyWithErrorHandler:
clearCache
getDylibHandlerWithError:
respondsToSelector:
T^v
recursiveMutexForXpcConnections
listener:shouldAcceptNewConnection:
name
numberWithUnsignedLong:
registerCacheRefresh:
removeAllObjects
stringByTrimmingCharactersInSet:
accessInstanceVariablesDirectly
```
