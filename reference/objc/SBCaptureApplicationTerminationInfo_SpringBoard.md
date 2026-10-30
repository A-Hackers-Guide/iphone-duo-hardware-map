# `SBCaptureApplicationTerminationInfo`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSString" _processName;
@"NSString" _buildVersion;
@"NSString" _terminationReason;
```

## Properties

```
@property (T@"NSString",R,C,N,V_processName) processName;
@property (T@"NSString",R,C,N,V_buildVersion) buildVersion;
@property (T@"NSString",R,C,N,V_terminationReason) terminationReason;
```

## Class methods

```
+[SBCaptureApplicationTerminationInfo supportsSecureCoding];
+[SBCaptureApplicationTerminationInfo __buildVersion];
```

## Instance methods

```
-[SBCaptureApplicationTerminationInfo buildVersion];
-[SBCaptureApplicationTerminationInfo processName];
-[SBCaptureApplicationTerminationInfo encodeWithCoder:];
-[SBCaptureApplicationTerminationInfo initWithCoder:];
-[SBCaptureApplicationTerminationInfo copyWithZone:];
-[SBCaptureApplicationTerminationInfo terminationReason];
-[SBCaptureApplicationTerminationInfo isEqual:];
-[SBCaptureApplicationTerminationInfo initWithProcessName:terminationReason:];
```
