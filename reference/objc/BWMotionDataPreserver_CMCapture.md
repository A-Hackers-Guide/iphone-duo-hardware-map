# `BWMotionDataPreserver`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSMutableData" _preservedISPMotionData;
Q _lengthOfInitialISPMotionData;
i _sampleCountOfInitialISPMotionData;
@"NSMutableData" _preservedISPHallData;
Q _lengthOfInitialISPHallData;
i _sampleCountOfInitialISPHallData;
@"NSString" _currentISPHallPortType;
```

## Class methods

```
+[BWMotionDataPreserver initialize];
```

## Instance methods

```
-[BWMotionDataPreserver dealloc];
-[BWMotionDataPreserver reset];
-[BWMotionDataPreserver initWithName:];
-[BWMotionDataPreserver prependPreservedMotionDataToSampleBuffer:];
-[BWMotionDataPreserver preserveMotionDataForSoonToBeDroppedSampleBuffer:];
```
