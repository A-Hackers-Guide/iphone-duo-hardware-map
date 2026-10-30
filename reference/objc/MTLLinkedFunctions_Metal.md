# `MTLLinkedFunctions`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 4 properties, 4 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _privateFunctions;
```

## Properties

```
@property (T@"NSArray",C,D,N) functions;
@property (T@"NSArray",C,D,N) binaryFunctions;
@property (T@"NSDictionary",C,D,N) groups;
@property (T@"NSArray",C,N,V_privateFunctions) privateFunctions;
```

## Class methods

```
+[MTLLinkedFunctions allocWithZone:];
+[MTLLinkedFunctions linkedFunctions];
+[MTLLinkedFunctions alloc];
```

## Instance methods

```
-[MTLLinkedFunctions reset];
-[MTLLinkedFunctions setPrivateFunctions:];
-[MTLLinkedFunctions privateFunctions];
-[MTLLinkedFunctions copyWithZone:];
```
