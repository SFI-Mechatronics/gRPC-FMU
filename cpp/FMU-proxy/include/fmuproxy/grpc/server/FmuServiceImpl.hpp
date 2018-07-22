/*
 * The MIT License
 *
 * Copyright 2017-2018 Norwegian University of Technology
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#ifndef FMU_PROXY_FMUSERVICEIMPL_HPP
#define FMU_PROXY_FMUSERVICEIMPL_HPP

#include "../common/definitions.pb.h"
#include "../common/service.grpc.pb.h"

#include "../../fmi/Fmu.hpp"

namespace fmuproxy {
    namespace grpc {
        namespace server {

            class FmuServiceImpl : public fmuproxy::grpc::FmuService::Service {

            private:
                fmuproxy::fmi::Fmu &m_fmu;

            public:

                FmuServiceImpl(fmuproxy::fmi::Fmu &fmu);

                ::grpc::Status
                GetModelDescriptionXml(::grpc::ServerContext *context, const ::google::protobuf::Empty *request,
                                       ::fmuproxy::grpc::Str *response) override;

                grpc::Status
                GetModelDescription(::grpc::ServerContext *context, const ::google::protobuf::Empty *request,
                                    ::fmuproxy::grpc::ModelDescription *response) override;

            };

        }
    }
}

#endif //FMU_PROXY_FMUSERVICEIMPL_HPP
