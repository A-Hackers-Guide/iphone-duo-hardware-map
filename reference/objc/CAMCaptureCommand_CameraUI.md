# `CAMCaptureCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSString" _reason;
@"NSArray" _subcommands;
```

## Properties

```
@property (T@"NSArray",C,N,V_subcommands) subcommands;
@property (T@"NSString",C,N,V_reason) reason;
@property (TB,R,N) requiresSessionModification;
@property (T@"NSString",R,C,N) sessionModificationLogReason;
@property (Td,R,N) sessionModificationMinimumExecutionTime;
@property (T@"NSDictionary",R,N) userInfo;
```

## Instance methods

```
-[CAMCaptureCommand requiresSessionModification];
-[CAMCaptureCommand init];
-[CAMCaptureCommand sessionModificationLogReason];
-[CAMCaptureCommand userInfo];
-[CAMCaptureCommand setReason:];
-[CAMCaptureCommand executeWithContext:];
-[CAMCaptureCommand reason];
-[CAMCaptureCommand sessionModificationMinimumExecutionTime];
-[CAMCaptureCommand copyWithZone:];
-[CAMCaptureCommand setSubcommands:];
-[CAMCaptureCommand addSubcommand:];
-[CAMCaptureCommand initWithSubcommands:];
-[CAMCaptureCommand removeSubcommand:];
-[CAMCaptureCommand subcommands];
```
