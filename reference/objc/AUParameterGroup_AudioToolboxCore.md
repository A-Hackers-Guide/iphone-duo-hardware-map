# `AUParameterGroup`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUParameterNode`
- Protocols: `NSSecureCoding`
- 2 instance variables, 3 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _children;
@"NSMutableDictionary" _childIndicesByIdentifier;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_childIndicesByIdentifier) childIndicesByIdentifier;
@property (T@"NSArray",R,N,V_children) children;
@property (T@"NSArray",R,N) allParameters;
```

## Class methods

```
+[AUParameterGroup supportsSecureCoding];
```

## Instance methods

```
-[AUParameterGroup _deserialize:fromSetFullState:];
-[AUParameterGroup _serialize:];
-[AUParameterGroup dealloc];
-[AUParameterGroup _indexChildren];
-[AUParameterGroup setChildIndicesByIdentifier:];
-[AUParameterGroup initWithID:name:children:];
-[AUParameterGroup copyNodeWithOffset:];
-[AUParameterGroup _observersChanged:deltaCount:];
-[AUParameterGroup allParameters];
-[AUParameterGroup childIndicesByIdentifier];
-[AUParameterGroup valueForKey:];
-[AUParameterGroup children];
-[AUParameterGroup encodeWithCoder:];
-[AUParameterGroup initWithCoder:];
-[AUParameterGroup isGroup];
-[AUParameterGroup initWithTemplate:identifier:name:addressOffset:];
-[AUParameterGroup initWithChildren:];
```
