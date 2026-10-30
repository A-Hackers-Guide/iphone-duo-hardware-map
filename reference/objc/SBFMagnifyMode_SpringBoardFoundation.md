# `SBFMagnifyMode`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`
- 3 instance variables, 7 properties, 15 instance methods, 2 class methods

## Instance variables

```
f _zoomFactor;
@"NSString" _name;
{CGSize="width"d"height"d} _size;
```

## Properties

```
@property (T{CGSize=dd},N,V_size) size;
@property (T@"NSString",&,N,V_name) name;
@property (Tf,N,V_zoomFactor) zoomFactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFMagnifyMode currentMagnifyMode];
+[SBFMagnifyMode magnifyModeWithSize:name:];
```

## Instance methods

```
-[SBFMagnifyMode zoomFactor];
-[SBFMagnifyMode setZoomFactor:];
-[SBFMagnifyMode succinctDescriptionBuilder];
-[SBFMagnifyMode init];
-[SBFMagnifyMode descriptionWithMultilinePrefix:];
-[SBFMagnifyMode size];
-[SBFMagnifyMode succinctDescription];
-[SBFMagnifyMode hash];
-[SBFMagnifyMode description];
-[SBFMagnifyMode setName:];
-[SBFMagnifyMode copyWithZone:];
-[SBFMagnifyMode isEqual:];
-[SBFMagnifyMode name];
-[SBFMagnifyMode setSize:];
-[SBFMagnifyMode descriptionBuilderWithMultilinePrefix:];
```
