# `NWURLSessionMultipartParser`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
B _isFirstBoundary;
B _didDeliverComplete;
i _parserState;
i _dispositionState;
@"NSString" _boundary;
@"<NWURLSessionResponseConsumer>" _responseConsumer;
@"NSObject<OS_dispatch_data>" _data;
@"NSMutableArray" _parts;
@"NWURLSessionMultipartBoundaryRecognizer" _boundaryRecognizer;
@"NWURLSessionMultipartHeaderRecognizer" _headerRecognizer;
@"NWURLSessionMultipartPartBoundarySuffixRecognizer" _boundarySuffixRecognizer;
@"NSMutableDictionary" _headers;
@"NSObject<OS_dispatch_queue>" _queue;
Q _boundaryPatternSize;
```
