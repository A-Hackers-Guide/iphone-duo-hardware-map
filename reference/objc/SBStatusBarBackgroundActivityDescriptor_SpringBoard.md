# `SBStatusBarBackgroundActivityDescriptor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
i _pid;
@"NSString" _backgroundActivityIdentifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_backgroundActivityIdentifier) backgroundActivityIdentifier;
@property (Ti,R,N,V_pid) pid;
```

## Instance methods

```
-[SBStatusBarBackgroundActivityDescriptor succinctDescriptionBuilder];
-[SBStatusBarBackgroundActivityDescriptor backgroundActivityIdentifier];
-[SBStatusBarBackgroundActivityDescriptor descriptionWithMultilinePrefix:];
-[SBStatusBarBackgroundActivityDescriptor succinctDescription];
-[SBStatusBarBackgroundActivityDescriptor pid];
-[SBStatusBarBackgroundActivityDescriptor hash];
-[SBStatusBarBackgroundActivityDescriptor description];
-[SBStatusBarBackgroundActivityDescriptor copyWithZone:];
-[SBStatusBarBackgroundActivityDescriptor isEqual:];
-[SBStatusBarBackgroundActivityDescriptor descriptionBuilderWithMultilinePrefix:];
-[SBStatusBarBackgroundActivityDescriptor initWithBackgroundActivityIdentifier:pid:];
```
