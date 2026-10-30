# `UISystemNavigationActionDestinationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`
- 4 instance variables, 8 properties, 11 instance methods, 4 class methods

## Instance variables

```
@"NSString" _title;
@"NSString" _bundleId;
@"NSURL" _URL;
@"NSString" _sceneIdentifier;
```

## Properties

```
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_bundleId) bundleId;
@property (T@"NSURL",C,N,V_URL) URL;
@property (T@"NSString",C,N,V_sceneIdentifier) sceneIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISystemNavigationActionDestinationContext systemNavigationActionContextWithTitle:andURL:];
+[UISystemNavigationActionDestinationContext systemNavigationActionContextWithTitle:bundleId:];
+[UISystemNavigationActionDestinationContext systemNavigationActionContextWithTitle:sceneIdentifier:];
+[UISystemNavigationActionDestinationContext systemNavigationActionContextWithURL:];
```

## Instance methods

```
-[UISystemNavigationActionDestinationContext debugDescription];
-[UISystemNavigationActionDestinationContext initWithXPCDictionary:];
-[UISystemNavigationActionDestinationContext setBundleId:];
-[UISystemNavigationActionDestinationContext setSceneIdentifier:];
-[UISystemNavigationActionDestinationContext sceneIdentifier];
-[UISystemNavigationActionDestinationContext encodeWithXPCDictionary:];
-[UISystemNavigationActionDestinationContext setURL:];
-[UISystemNavigationActionDestinationContext title];
-[UISystemNavigationActionDestinationContext bundleId];
-[UISystemNavigationActionDestinationContext setTitle:];
-[UISystemNavigationActionDestinationContext URL];
```
