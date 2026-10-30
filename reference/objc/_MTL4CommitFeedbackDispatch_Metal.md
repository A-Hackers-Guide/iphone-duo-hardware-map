# `_MTL4CommitFeedbackDispatch`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{vector<void (^)(id<MTL4CommitFeedback>), std::allocator<void (^)(id<MTL4CommitFeedback>)>>="__begin_"^@?"__end_"^@?""{?="__cap_"^@?}} _feedbackNotificationBlocks;
```

## Instance methods

```
-[_MTL4CommitFeedbackDispatch dealloc];
-[_MTL4CommitFeedbackDispatch addFeedbackHandler:];
-[_MTL4CommitFeedbackDispatch executeBlocksWithCommitFeedback:];
```
