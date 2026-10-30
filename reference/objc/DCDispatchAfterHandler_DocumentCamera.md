# `DCDispatchAfterHandler`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _identifierBlockMap;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_identifierBlockMap) identifierBlockMap;
```

## Class methods

```
+[DCDispatchAfterHandler appLifeCycleHandler];
```

## Instance methods

```
-[DCDispatchAfterHandler init];
-[DCDispatchAfterHandler cancelAll];
-[DCDispatchAfterHandler cancelBlocksWithStringIdentifier:];
-[DCDispatchAfterHandler dispatchAfter:stringIdentifier:withBlock:];
-[DCDispatchAfterHandler identifierBlockMap];
-[DCDispatchAfterHandler identifierForStringIdentifier:];
-[DCDispatchAfterHandler setIdentifierBlockMap:];
```
