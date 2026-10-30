# `TUMomentsProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _remoteMomentsAvailable;
q _streamToken;
@"NSString" _requesterID;
@"NSDictionary" _remoteIDSDestinations;
```

## Properties

```
@property (Tq,R,N,V_streamToken) streamToken;
@property (T@"NSString",R,C,N,V_requesterID) requesterID;
@property (T@"NSDictionary",R,C,N,V_remoteIDSDestinations) remoteIDSDestinations;
@property (TB,R,N,GisRemoteMomentsAvailable,V_remoteMomentsAvailable) remoteMomentsAvailable;
```

## Instance methods

```
-[TUMomentsProvider streamToken];
-[TUMomentsProvider description];
-[TUMomentsProvider isEqualToProvider:];
-[TUMomentsProvider initWithCall:];
-[TUMomentsProvider initWithConversation:];
-[TUMomentsProvider isRemoteMomentsAvailable];
-[TUMomentsProvider remoteIDSDestinations];
-[TUMomentsProvider requesterID];
```
