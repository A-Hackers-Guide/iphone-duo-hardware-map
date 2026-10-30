# `LARightStore`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<LAKeyStore>" _keyStore;
@"NSObject<OS_dispatch_queue>" _workQueue;
Q _instanceID;
```

## Class methods

```
+[LARightStore sharedStore];
```

## Instance methods

```
-[LARightStore init];
-[LARightStore dealloc];
-[LARightStore description];
-[LARightStore removeAllRightsWithCompletion:];
-[LARightStore removeRight:completion:];
-[LARightStore removeRightForIdentifier:completion:];
-[LARightStore rightForIdentifier:completion:];
-[LARightStore saveRight:identifier:completion:];
-[LARightStore saveRight:identifier:secret:completion:];
```
