# `LAPersistedRight`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LARight`
- 2 instance variables, 2 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _secrets;
@"NSArray" _privateKeys;
```

## Properties

```
@property (T@"LAPrivateKey",R,N) key;
@property (T@"LASecret",R,N) secret;
```

## Instance methods

```
-[LAPersistedRight key];
-[LAPersistedRight secret];
-[LAPersistedRight initWithIdentifier:accessKey:privateKeys:secrets:];
```
