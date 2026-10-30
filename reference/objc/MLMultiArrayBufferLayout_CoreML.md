# `MLMultiArrayBufferLayout`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CoreML::MultiArrayBufferLayout, std::default_delete<CoreML::MultiArrayBufferLayout>>=""{?="__ptr_"^{MultiArrayBufferLayout}}} _bufferLayout;
```

## Properties

```
@property (Tq,R,N) count;
@property (T@"NSArray",R,N) shape;
@property (T@"NSArray",R,N) strides;
```

## Instance methods

```
-[MLMultiArrayBufferLayout shape];
-[MLMultiArrayBufferLayout count];
-[MLMultiArrayBufferLayout strides];
-[MLMultiArrayBufferLayout description];
-[MLMultiArrayBufferLayout initWithShape:strides:];
-[MLMultiArrayBufferLayout isSubspaceOfBufferLayout:];
-[MLMultiArrayBufferLayout offsetOfScalarAtIndex:contiguousScalars:];
```
