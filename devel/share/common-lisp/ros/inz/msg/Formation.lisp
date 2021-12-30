; Auto-generated. Do not edit!


(cl:in-package inz-msg)


;//! \htmlinclude Formation.msg.html

(cl:defclass <Formation> (roslisp-msg-protocol:ros-message)
  ((Lx
    :reader Lx
    :initarg :Lx
    :type cl:float
    :initform 0.0)
   (Ly
    :reader Ly
    :initarg :Ly
    :type cl:float
    :initform 0.0)
   (L
    :reader L
    :initarg :L
    :type cl:float
    :initform 0.0))
)

(cl:defclass Formation (<Formation>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Formation>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Formation)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name inz-msg:<Formation> is deprecated: use inz-msg:Formation instead.")))

(cl:ensure-generic-function 'Lx-val :lambda-list '(m))
(cl:defmethod Lx-val ((m <Formation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:Lx-val is deprecated.  Use inz-msg:Lx instead.")
  (Lx m))

(cl:ensure-generic-function 'Ly-val :lambda-list '(m))
(cl:defmethod Ly-val ((m <Formation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:Ly-val is deprecated.  Use inz-msg:Ly instead.")
  (Ly m))

(cl:ensure-generic-function 'L-val :lambda-list '(m))
(cl:defmethod L-val ((m <Formation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:L-val is deprecated.  Use inz-msg:L instead.")
  (L m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Formation>) ostream)
  "Serializes a message object of type '<Formation>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'Lx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'Ly))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'L))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Formation>) istream)
  "Deserializes a message object of type '<Formation>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Lx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Ly) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'L) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Formation>)))
  "Returns string type for a message object of type '<Formation>"
  "inz/Formation")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Formation)))
  "Returns string type for a message object of type 'Formation"
  "inz/Formation")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Formation>)))
  "Returns md5sum for a message object of type '<Formation>"
  "d31db8d8681c59a19527284d3d5b77c3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Formation)))
  "Returns md5sum for a message object of type 'Formation"
  "d31db8d8681c59a19527284d3d5b77c3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Formation>)))
  "Returns full string definition for message of type '<Formation>"
  (cl:format cl:nil "float32 Lx~%float32 Ly~%float32 L~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Formation)))
  "Returns full string definition for message of type 'Formation"
  (cl:format cl:nil "float32 Lx~%float32 Ly~%float32 L~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Formation>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Formation>))
  "Converts a ROS message object to a list"
  (cl:list 'Formation
    (cl:cons ':Lx (Lx msg))
    (cl:cons ':Ly (Ly msg))
    (cl:cons ':L (L msg))
))
