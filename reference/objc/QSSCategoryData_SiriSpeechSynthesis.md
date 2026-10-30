# `QSSCategoryData`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{CategoryData=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) category_name;
@property (T@"NSArray",R,N) category_data;
```

## Instance methods

```
-[QSSCategoryData copyWithZone:];
-[QSSCategoryData addObjectToBuffer:];
-[QSSCategoryData flatbuffData];
-[QSSCategoryData initAndVerifyWithFlatbuffData:];
-[QSSCategoryData initWithFlatbuffData:];
-[QSSCategoryData initWithFlatbuffData:root:];
-[QSSCategoryData initWithFlatbuffData:root:verify:];
-[QSSCategoryData category_data];
-[QSSCategoryData category_name];
```
