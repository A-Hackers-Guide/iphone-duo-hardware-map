# `SBJSONCoder`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSCoder`
- Protocols: `BSXPCEncoding`
- 2 instance variables, 4 properties, 34 instance methods, 0 class methods

## Instance variables

```
@ _root;
@"NSMutableArray" _contextStack;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBJSONCoder encodeObject:];
-[SBJSONCoder encodeDataObject:];
-[SBJSONCoder encodeXPCObject:forKey:];
-[SBJSONCoder encodeUInt64:forKey:];
-[SBJSONCoder encodeCGPoint:forKey:];
-[SBJSONCoder encodeConditionalObject:forKey:];
-[SBJSONCoder encodeDouble:forKey:];
-[SBJSONCoder allowsKeyedCoding];
-[SBJSONCoder encodeRootObject:];
-[SBJSONCoder init];
-[SBJSONCoder encodeBool:forKey:];
-[SBJSONCoder encodeDictionary:forKey:];
-[SBJSONCoder encodeInt32:forKey:];
-[SBJSONCoder encodeCGRect:forKey:];
-[SBJSONCoder encodeObject:forKey:];
-[SBJSONCoder encodeCGSize:forKey:];
-[SBJSONCoder encodeInteger:forKey:];
-[SBJSONCoder encodeStruct:withObjCType:forKey:];
-[SBJSONCoder encodeBytes:length:forKey:];
-[SBJSONCoder encodeInt64:forKey:];
-[SBJSONCoder encodeValueOfObjCType:at:];
-[SBJSONCoder encodeFloat:forKey:];
-[SBJSONCoder encodeInt:forKey:];
-[SBJSONCoder rootObject];
-[SBJSONCoder _setObject:forKey:];
-[SBJSONCoder encodeCollection:forKey:];
-[SBJSONCoder encodeCGAffineTransform:forKey:];
-[SBJSONCoder encodeCGVector:forKey:];
-[SBJSONCoder encodeDirectionalEdgeInsets:forKey:];
-[SBJSONCoder encodeUIEdgeInsets:forKey:];
-[SBJSONCoder encodeUIOffset:forKey:];
-[SBJSONCoder _currentContext];
-[SBJSONCoder _popContext];
-[SBJSONCoder _pushDictionaryContextForKey:];
```
