# `SBHApplication` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBLeafIconDataSource`, `NSObject`
- 0 instance variables, 13 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) bundleIdentifier;
@property (T@"NSURL",R,N) bundleURL;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",?,R,C,N) vendorName;
@property (T@"NSArray",?,R,N) tags;
@property (TB,?,R,N) hasHiddenTag;
@property (T@"NSString",?,R,C,N) iconIdentifier;
@property (TB,?,R,N,GisSystemApplication) systemApplication;
@property (TB,?,R,N,GisInternalApplication) internalApplication;
@property (TB,?,R,N,GisAppleApplication) appleApplication;
@property (TB,?,R,N,GisAppClip) appClip;
@property (TB,?,R,N,GisPlaceholder) placeholder;
@property (T@,?,&,N) badgeValue;
```

## Instance methods

```
-[SBHApplication bundleURL];
-[SBHApplication displayName];
-[SBHApplication bundleIdentifier];
-[SBHApplication vendorName];
-[SBHApplication badgeValue];
-[SBHApplication setBadgeValue:];
-[SBHApplication hasHiddenTag];
-[SBHApplication isPlaceholder];
-[SBHApplication tags];
-[SBHApplication possibleUserTapDidCancel];
-[SBHApplication isAppleApplication];
-[SBHApplication possibleUserTapBeganWithAbsoluteTime:andContinuousTime:];
-[SBHApplication iconIdentifier];
-[SBHApplication isInternalApplication];
-[SBHApplication isSystemApplication];
-[SBHApplication isAppClip];
```
