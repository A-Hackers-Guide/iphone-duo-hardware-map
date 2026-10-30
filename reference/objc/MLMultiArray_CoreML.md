# `MLMultiArray`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 12 properties, 61 instance methods, 19 class methods

## Instance variables

```
{unique_ptr<StorageManager, std::default_delete<StorageManager>>=""{?="__ptr_"^{StorageManager}}} _storageManager;
@"NSArray" _shape;
```

## Properties

```
@property (Tr^v,R,N) bytes;
@property (T^v,R,N) mutableBytes;
@property (TQ,R,N) numberOfBytesPerElement;
@property (TB,R,N,GisContiguous) contiguous;
@property (TB,R,N) backingPixelBufferWasLocked;
@property (T@"<MTLBuffer>",R,N) mtlBuffer;
@property (T^v,R,N) dataPointer;
@property (Tq,R,N) dataType;
@property (T@"NSArray",R,N,V_shape) shape;
@property (T@"NSArray",R,N) strides;
@property (Tq,R,N) count;
@property (T^{__CVBuffer=},R,N) pixelBuffer;
```

## Class methods

```
+[MLMultiArray supportsSecureCoding];
+[MLMultiArray stringForDataType:];
+[MLMultiArray _multiArrayByConcatenatingMultiArrays:alongAxis:dataType:];
+[MLMultiArray _shapeOfNestedArray:error:];
+[MLMultiArray cppStorageOrder:];
+[MLMultiArray doubleMatrixWithValues:error:];
+[MLMultiArray doubleMultiArrayWithCopyOfMultiArray:];
+[MLMultiArray doubleMultiArrayWithShape:valueArray:error:];
+[MLMultiArray doubleVectorWithValues:];
+[MLMultiArray float32MatrixWithValues:error:];
+[MLMultiArray getShapeOfArrayOfSameLengthArrays:numberOfRows:numberOfColumns:error:];
+[MLMultiArray multiArrayByConcatenatingMultiArrays:alongAxis:dataType:];
+[MLMultiArray multiArrayOwningBufferObjectOfPort:error:];
+[MLMultiArray newMultiArrayForState:strides:dtype:error:];
+[MLMultiArray pixelBufferBGRA8FromMultiArrayCHW:channelOrderIsBGR:error:];
+[MLMultiArray pixelBufferGray16HalfFromMultiArrayHW:error:];
+[MLMultiArray pixelBufferGray8FromMultiArrayHW:error:];
+[MLMultiArray validateMultiArrays:forConcatenatingAlongAxis:normalizedAxis:reason:];
+[MLMultiArray validateNestedArray:error:];
```

## Instance methods

```
-[MLMultiArray setObject:atIndexedSubscript:];
-[MLMultiArray pixelBuffer];
-[MLMultiArray renderTo32BGRAPixelBuffer:channelOrderIsBGR:error:];
-[MLMultiArray copyIntoMultiArray:error:];
-[MLMultiArray getContiguousFirstMajorFloat32BufferWithHandler:];
-[MLMultiArray initWithBytesNoCopy:shape:dataType:strides:deallocator:mutableShapedBufferProvider:error:];
-[MLMultiArray backingPixelBufferWasLocked];
-[MLMultiArray shape];
-[MLMultiArray float32Pointer];
-[MLMultiArray multiArrayBuffer];
-[MLMultiArray init];
-[MLMultiArray debugQuickLookObject];
-[MLMultiArray numberOfBytesPerElement];
-[MLMultiArray squeezeDimensions:error:];
-[MLMultiArray objectAtIndexedSubscript:];
-[MLMultiArray renderToOneComponent16HalfPixelBuffer:error:];
-[MLMultiArray initWithScalars:shape:dataType:];
-[MLMultiArray numberAtOffset:];
-[MLMultiArray isContiguousInOrder:];
-[MLMultiArray initWithMultiArrayBuffer:];
-[MLMultiArray initWithPixelBuffer:shape:strides:mutableShapedBufferProvider:];
-[MLMultiArray numberArray];
-[MLMultiArray isEqualToMultiArray:];
-[MLMultiArray count];
-[MLMultiArray sliceAtOrigin:shape:squeeze:error:];
-[MLMultiArray initWithPixelBuffer:shape:];
-[MLMultiArray initWithArray:dataType:];
-[MLMultiArray objectForKeyedSubscript:];
-[MLMultiArray initWithBytesNoCopy:shape:dataType:strides:mutableShapedBufferProvider:];
-[MLMultiArray strides];
-[MLMultiArray renderToOneComponent8PixelBuffer:error:];
-[MLMultiArray renderToCVPixelBuffer:channelOrderIsBGR:error:];
-[MLMultiArray dataPointer];
-[MLMultiArray offsetForKeyedSubscript:];
-[MLMultiArray isContiguous];
-[MLMultiArray doublePointer];
-[MLMultiArray encodeWithCoder:];
-[MLMultiArray getBytesWithHandler:];
-[MLMultiArray vectorizeIntoMultiArray:storageOrder:error:];
-[MLMultiArray initWithShape:dataType:storageOrder:error:];
-[MLMultiArray dataType];
-[MLMultiArray multiArrayViewExpandingDimensionsAtAxis:];
-[MLMultiArray description];
-[MLMultiArray transferToMultiArray:];
-[MLMultiArray setRangeWithRawData:destIndex:error:];
-[MLMultiArray squeeze];
-[MLMultiArray initWithCoder:];
-[MLMultiArray mutableBytes];
-[MLMultiArray initWithPixelBuffer:shape:strides:];
-[MLMultiArray isEqual:];
-[MLMultiArray getMutableBytesWithHandler:];
-[MLMultiArray setObject:forKeyedSubscript:];
-[MLMultiArray bytes];
-[MLMultiArray initWithShape:dataType:storageOrder:bufferAlignment:];
-[MLMultiArray initWithShape:dataType:error:];
-[MLMultiArray initWithDataPointer:shape:dataType:strides:deallocator:error:];
-[MLMultiArray setNumber:atOffset:];
-[MLMultiArray initWithMultiArrayBuffer:mutableShapedBufferProvider:];
-[MLMultiArray fillWithNumber:];
-[MLMultiArray initWithShape:dataType:strides:];
-[MLMultiArray mtlBuffer];
```
