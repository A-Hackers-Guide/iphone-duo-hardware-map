# `PKHashtagItem`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKDetectionItem`
- 0 instance variables, 3 properties, 12 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",R,N) hashtagResult;
@property (T@"NSUUID",R,N) hashtagUUID;
@property (TB,R,N) active;
```

## Class methods

```
+[PKHashtagItem hashtagItemWithQueryItem:sessionManager:];
```

## Instance methods

```
-[PKHashtagItem active];
-[PKHashtagItem setActive:];
-[PKHashtagItem strokeColor];
-[PKHashtagItem hash];
-[PKHashtagItem description];
-[PKHashtagItem isEqual:];
-[PKHashtagItem _actionNameForActivation:];
-[PKHashtagItem _baselinePath];
-[PKHashtagItem clearActiveInDrawing:];
-[PKHashtagItem hashtagResult];
-[PKHashtagItem hashtagUUID];
-[PKHashtagItem invalidateUUID];
```
