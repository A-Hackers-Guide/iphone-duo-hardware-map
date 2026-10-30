# `/System/Library/PrivateFrameworks/AccessorySensorManagerDarwin_Private.framework/AccessorySensorManagerDarwin_Private`

iOS 27.2 dyld shared cache image. Version `20.27.0.0.0`. **[DSC]**

## Linked libraries (7)

- `/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`
- `/System/Library/PrivateFrameworks/AccessorySensorManagerDefines_Private.framework/AccessorySensorManagerDefines_Private`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

## Objective-C: 4 classes, 0 protocols, 19 methods, 3 properties

### Class pages

Every class and protocol, with its methods: [`ASMImageProcessingHelper`](../objc/ASMImageProcessingHelper_AccessorySensorManagerDarwin_Private.md), [`ASMPolarisResourceProvider`](../objc/ASMPolarisResourceProvider_AccessorySensorManagerDarwin_Private.md), [`ASMPowerAssertion`](../objc/ASMPowerAssertion_AccessorySensorManagerDarwin_Private.md), [`ASMSignpost`](../objc/ASMSignpost_AccessorySensorManagerDarwin_Private.md)

### Classes

`ASMImageProcessingHelper`, `ASMPolarisResourceProvider`, `ASMPowerAssertion`, `ASMSignpost`

### Properties

```
@property (T@?,C,N,V_resourceStartHandler) resourceStartHandler;
@property (T@?,C,N,V_resourceStopHandler) resourceStopHandler;
@property (T@"NSObject<OS_os_log>",&,N,V_asmLogInstance) asmLogInstance;
```

## Strings (18)

```
v8@?0
yes
no
IOPMAssertionRelease failed: %d
com.apple.ASMPolarisResourceProvider.daemon.queue
com.apple.AccessorySensorManager.signpost
Acquiring power assertion '%@' (refCount=%lu)
IOPMAssertionDeclareSystemActivity failed: %d
-[ASMPowerAssertion releaseAssertion]
Acquired power assertion '%@' (id=%u, sleepReverted=%s)
Releasing power assertion '%@' (refCount=%lu)
Released power assertion '%@' (id=%u)
Auto-releasing power assertion '%@' after %.1fs timeout
ASMPowerAssertion
ASMSignpost
-[ASMPowerAssertion acquireAssertion]
-[ASMPowerAssertion _resetTimer]
com.apple.AccessorySensorManager
```
