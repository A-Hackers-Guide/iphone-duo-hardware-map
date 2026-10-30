# `MLShufflingBatchProvider`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLBatchProvider`
- 3 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
{vector<long, std::allocator<long>>="__begin_"^q"__end_"^q""{?="__cap_"^q}} indices;
{linear_congruential_engine<unsigned int, 48271U, 0U, 2147483647U>="__x_"I} randomNumberGenerator;
@"<MLBatchProvider>" _batchProvider;
```

## Properties

```
@property (T@"<MLBatchProvider>",&,V_batchProvider) batchProvider;
@property (Tq,R,N) count;
```

## Instance methods

```
-[MLShufflingBatchProvider count];
-[MLShufflingBatchProvider shuffle];
-[MLShufflingBatchProvider batchProvider];
-[MLShufflingBatchProvider featuresAtIndex:];
-[MLShufflingBatchProvider initWithBatchProvider:seed:];
-[MLShufflingBatchProvider setBatchProvider:];
```
