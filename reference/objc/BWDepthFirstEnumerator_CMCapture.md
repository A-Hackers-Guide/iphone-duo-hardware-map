# `BWDepthFirstEnumerator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNodeEnumerator`
- 4 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
i _ordering;
@"NSArray" _sourceNodes;
@"NSMutableArray" _stack;
Q _currentSourceIndex;
```

## Instance methods

```
-[BWDepthFirstEnumerator nextObject];
-[BWDepthFirstEnumerator dealloc];
-[BWDepthFirstEnumerator initWithGraph:vertexOrdering:];
-[BWDepthFirstEnumerator initWithSourceNodes:vertexOrdering:];
```
