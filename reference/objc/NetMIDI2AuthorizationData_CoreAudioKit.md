# `NetMIDI2AuthorizationData`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
i _authenticationMethod;
@"NSString" _username;
@"NSString" _password;
@"NSString" _sharedSecret;
```

## Properties

```
@property (Ti,N,V_authenticationMethod) authenticationMethod;
@property (T@"NSString",&,N,V_username) username;
@property (T@"NSString",&,N,V_password) password;
@property (T@"NSString",&,N,V_sharedSecret) sharedSecret;
```

## Class methods

```
+[NetMIDI2AuthorizationData fromDictionary:];
```

## Instance methods

```
-[NetMIDI2AuthorizationData toDictionary];
-[NetMIDI2AuthorizationData init];
-[NetMIDI2AuthorizationData username];
-[NetMIDI2AuthorizationData setUsername:];
-[NetMIDI2AuthorizationData setPassword:];
-[NetMIDI2AuthorizationData password];
-[NetMIDI2AuthorizationData authenticationMethod];
-[NetMIDI2AuthorizationData initWithUsername:password:];
-[NetMIDI2AuthorizationData setSharedSecret:];
-[NetMIDI2AuthorizationData sharedSecret];
-[NetMIDI2AuthorizationData setAuthenticationMethod:];
-[NetMIDI2AuthorizationData initWithMethod:username:password:sharedSecret:];
-[NetMIDI2AuthorizationData initWithSharedSecret:];
```
