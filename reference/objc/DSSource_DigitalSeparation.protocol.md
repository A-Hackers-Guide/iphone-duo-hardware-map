# `DSSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) name;
@property (T@"NSArray",?,R,C,N) resourceNames;
```

## Instance methods

```
-[DSSource name];
-[DSSource stopAllSharingWithCompletion:];
-[DSSource fetchSharedResourcesWithCompletion:];
-[DSSource stopSharing:withCompletion:];
-[DSSource stopSharingWithParticipant:completion:];
-[DSSource fetchSharedResourcesWithName:completion:];
-[DSSource resourceNames];
-[DSSource stopSharingResourcesWithName:completion:];
-[DSSource stopSharingWithParticipant:forResourceName:withCompletion:];
-[DSSource stopSharingWithParticipants:completion:];
-[DSSource updateParticipantAccessLevelTo:onResource:withCompletion:];
-[DSSource updateVisibilityTo:onResource:withCompletion:];
```
