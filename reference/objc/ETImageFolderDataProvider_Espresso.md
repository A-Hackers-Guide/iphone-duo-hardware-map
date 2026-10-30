# `ETImageFolderDataProvider`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ETDataProvider`
- 9 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
{vector<std::pair<NSString *, unsigned long>, std::allocator<std::pair<NSString *, unsigned long>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} samples;
{vector<NSString *, std::allocator<NSString *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} classes;
{shared_ptr<Espresso::blob_cpu>="__ptr_"^{blob_cpu}"__cntrl_"^{__shared_weak_count}} labelBlob;
@"NSString" imageTensorName;
@"NSString" labelTensorName;
@"NSArray" labelShape;
{linear_congruential_engine<unsigned int, 48271U, 0U, 2147483647U>="__x_"I} randomgen;
@"ETImagePreprocessor" imageProcessor;
B shuffleBeforeEpoch;
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
-[ETImageFolderDataProvider numberOfDataPoints];
-[ETImageFolderDataProvider prepareForEpoch];
-[ETImageFolderDataProvider dataPointAtIndex:error:];
-[ETImageFolderDataProvider initWithFolder:forImageTensor:andLabelTensor:shuffleBeforeEachEpoch:shuffleRandomSeed:withImagePreprocessParams:];
```
