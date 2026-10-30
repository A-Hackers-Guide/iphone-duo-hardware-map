# `DCSandboxExtension`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _canAccessFileURL;
B _shouldIssueSandboxExtensionWhenEncoding;
@"NSURL" _fileURL;
q _sandboxExtensionHandle;
```

## Properties

```
@property (TB,R,N,V_shouldIssueSandboxExtensionWhenEncoding) shouldIssueSandboxExtensionWhenEncoding;
@property (Tq,N,V_sandboxExtensionHandle) sandboxExtensionHandle;
@property (TB,R,N,V_canAccessFileURL) canAccessFileURL;
@property (T@"NSURL",R,N,V_fileURL) fileURL;
```

## Class methods

```
+[DCSandboxExtension supportsSecureCoding];
```

## Instance methods

```
-[DCSandboxExtension sandboxExtensionHandle];
-[DCSandboxExtension fileURL];
-[DCSandboxExtension initWithFileURL:];
-[DCSandboxExtension dealloc];
-[DCSandboxExtension setSandboxExtensionHandle:];
-[DCSandboxExtension encodeWithCoder:];
-[DCSandboxExtension relinquish];
-[DCSandboxExtension initWithCoder:];
-[DCSandboxExtension canAccessFileURL];
-[DCSandboxExtension shouldIssueSandboxExtensionWhenEncoding];
```
