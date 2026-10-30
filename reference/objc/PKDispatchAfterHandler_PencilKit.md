# `PKDispatchAfterHandler`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
+[PKDispatchAfterHandler appLifeCycleHandler];
```

## Instance methods

```
-[PKDispatchAfterHandler init];
-[PKDispatchAfterHandler cancelAll];
-[PKDispatchAfterHandler cancelBlocksWithStringIdentifier:];
-[PKDispatchAfterHandler dispatchAfter:stringIdentifier:withBlock:];
-[PKDispatchAfterHandler identifierBlockMap];
-[PKDispatchAfterHandler identifierForStringIdentifier:];
-[PKDispatchAfterHandler setIdentifierBlockMap:];
```
