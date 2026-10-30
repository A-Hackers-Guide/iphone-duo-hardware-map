# `TUSandboxExtendedURL`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 21 instance methods, 1 class methods

## Instance variables

```
i _pid;
@"NSURL" _URL;
@"NSString" _sandboxExtensionClass;
@"NSString" _sandboxExtensionToken;
q _sandboxExtensionHandle;
```

## Properties

```
@property (T@"NSURL",&,N,V_URL) URL;
@property (T@"NSString",C,N,V_sandboxExtensionToken) sandboxExtensionToken;
@property (Tq,N,V_sandboxExtensionHandle) sandboxExtensionHandle;
@property (Ti,N,V_pid) pid;
@property (T@"NSString",C,N,V_sandboxExtensionClass) sandboxExtensionClass;
```

## Class methods

```
+[TUSandboxExtendedURL supportsSecureCoding];
```

## Instance methods

```
-[TUSandboxExtendedURL setPid:];
-[TUSandboxExtendedURL sandboxExtensionHandle];
-[TUSandboxExtendedURL init];
-[TUSandboxExtendedURL dealloc];
-[TUSandboxExtendedURL setSandboxExtensionHandle:];
-[TUSandboxExtendedURL pid];
-[TUSandboxExtendedURL sandboxExtensionClass];
-[TUSandboxExtendedURL setURL:];
-[TUSandboxExtendedURL encodeWithCoder:];
-[TUSandboxExtendedURL hash];
-[TUSandboxExtendedURL description];
-[TUSandboxExtendedURL initWithCoder:];
-[TUSandboxExtendedURL isEqual:];
-[TUSandboxExtendedURL initWithURL:];
-[TUSandboxExtendedURL URL];
-[TUSandboxExtendedURL sandboxExtensionToken];
-[TUSandboxExtendedURL setSandboxExtensionToken:];
-[TUSandboxExtendedURL _issueSandboxExtensionWithClass:];
-[TUSandboxExtendedURL initWithURL:withExtensionType:];
-[TUSandboxExtendedURL isEqualToSandboxExtendedURL:];
-[TUSandboxExtendedURL setSandboxExtensionClass:];
```
