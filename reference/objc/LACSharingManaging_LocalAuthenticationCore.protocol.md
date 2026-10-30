# `LACSharingManaging` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 1 properties, 6 instance methods, 1 class methods

## Properties

```
@property (T@"<LACSharingManagerDelegate>",W,N) delegate;
```

## Class methods

```
+[LACSharingManaging isSharingError:];
```

## Instance methods

```
-[LACSharingManaging setDelegate:];
-[LACSharingManaging delegate];
-[LACSharingManaging authenticateWithRequest:];
-[LACSharingManaging canAuthenticateWithCompanion:completion:];
-[LACSharingManaging cancelSessionWithID:];
-[LACSharingManaging pairedDevicesForCompanion:completion:];
```
