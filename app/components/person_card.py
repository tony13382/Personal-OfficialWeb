class PersonCard:
    def __str__(self):
        return """
<div class="card shadow rounded-basic mb-4">
    <div class="card-body p-4">
        <div class="col-12">
            <div class="d-flex justify-content-center">
                <img src="/assets/imgs/index/myHead.webp" alt="my personal picture" width="120px" class="bordre-1 rounded-circle">
            </div>
            <h2 class="fs-4 text-SkyHeavyBlue text-center mt-2">
                呂亮進
            </h2>
            <p class="text-center text-black-50">後端開發／AI 工程師</p>
        </div>
        <div class="d-grid gap-2">
            <a target="_blank" type="button" class="btn btn-theme rounded-pill" href="/assets/file/rv/RV(Data_Science).pdf">
                我的履歷
            </a>
            <a type="button" class="btn btn-outline-theme rounded-pill" data-bs-toggle="modal" data-bs-target="#shareModel" data-bs-trigger="hover focus" data-bs-content="QR Code" data-bs-placement="bottom">聯絡我
            </a>
        </div>
    </div>
</div>
"""


class MoreModal:
    def __str__(self):
        return """
<!-- Modal -->
<div class="modal fade" id="shareModel" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
    aria-labelledby="shareModelLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered p-2" style="max-width: 800px;">
        <div class="modal-content rounded-basic">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="shareModelLabel">聯絡我</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body h-auto">
                <div class="row">
                    <div class="col-12 col-md-6">
                        <div class="d-grid gap-2 text" style="font-size: 1.2rem;">
                            <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                href="mailto:liangchinlu@gmail.com" target="_blank">
                                <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                    <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                        style="height: 48px; width: 48px; background-color: #b5f5ec; color: #08979c;">
                                        <i class="bi bi-envelope-fill"></i>
                                    </div>
                                    <div class="ms-3 fs-6">
                                        <p class="m-0 fw-bolder">Email</p>
                                        <p class="m-0 text-black-50">liangchinlu@gmail.com</p>
                                    </div>
                                </div>
                            </a>
                            <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                href="https://www.facebook.com/tony13382/" target="_blank">
                                <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                    <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                        style="height: 48px; width: 48px; background-color: #bae0ff; color: #0958d9;">
                                        <i class="bi bi-facebook"></i>
                                    </div>
                                    <div class="ms-3 fs-6">
                                        <p class="m-0 fw-bolder">Facebook</p>
                                        <p class="m-0 text-black-50">呂亮進 （양진）</p>
                                    </div>
                                </div>
                            </a>
                            <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                href="https://www.instagram.com/liang_chin_ml/" target="_blank">
                                <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                    <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                        style="height: 48px; width: 48px; background-color: #efdbff; color: #531dab;">
                                        <i class="bi bi-instagram"></i>
                                    </div>
                                    <div class="ms-3 fs-6">
                                        <p class="m-0 fw-bolder">Instagram</p>
                                        <p class="m-0 text-black-50">@liang_chin_ml</p>
                                    </div>
                                </div>
                            </a>
                            <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                href="https://www.linkedin.com/in/liang-chin-lu" target="_blank">
                                <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                    <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                        style="height: 48px; width: 48px; background-color: #d6e4ff; color: #1d39c4;">
                                        <i class="bi bi-linkedin"></i>
                                    </div>
                                    <div class="ms-3 fs-6">
                                        <p class="m-0 fw-bolder">LinkedIn</p>
                                        <p class="m-0 text-black-50">呂亮進 (Liang-Chin,Lu)</p>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                    <div class="col-12 col-md-6">
                        <div class="d-grid gap-2 text" style="font-size: 1.2rem;">
                            <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                href="https://github.com/tony13382" target="_blank">
                                <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                    <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                        style="height: 48px; width: 48px; background-color: #f5f5f5; color: #262626;">
                                        <i class="bi bi-github"></i>
                                    </div>
                                    <div class="ms-3 fs-6">
                                        <p class="m-0 fw-bolder">GitHub</p>
                                        <p class="m-0 text-black-50">tony13382</p>
                                    </div>
                                </div>
                            </a>
                            <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                href="https://meowlu.notion.site/Liang-Chin-ML-12e7c67f7f2d47249f0111882d932663"
                                target="_blank">
                                <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                    <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                        style="height: 48px; width: 48px; background-color: #fff1b8; color: #d48806;">
                                        <i class="bi bi-journal-bookmark-fill"></i>
                                    </div>
                                    <div class="ms-3 fs-6">
                                        <p class="m-0 fw-bolder">Notion 知識站</p>
                                        <p class="m-0 text-black-50">數位海洋．ML個人學習庫</p>
                                    </div>
                                </div>
                            </a>
                            <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                href="https://learn.lianglu.uk/" target="_blank">
                                <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                    <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                        style="height: 48px; width: 48px; background-color: #ffd6e7; color: #c41d7f;">
                                        <i class="bi bi-bookmark-heart-fill"></i>
                                    </div>
                                    <div class="ms-3 fs-6">
                                        <p class="m-0 fw-bolder">知識推薦獲取來源</p>
                                        <p class="m-0 text-black-50">IG／YT／FB／Mail／Web</p>
                                    </div>
                                </div>
                            </a>
                            <a class="text-decoration-none grayBlockHover rounded text-dark p-2"
                                href="http://portaly.cc/liang_chin_ml" target="_blank">
                                <div class="d-flex flex-row align-items-center px-2 py-2 rounded-inline-basic">
                                    <div class="d-flex align-items-center justify-content-center fs-3 rounded-circle"
                                        style="height: 48px; width: 48px; background-color: #d9f7be; color: #389e0d;">
                                        <i class="bi bi-three-dots"></i>
                                    </div>
                                    <div class="ms-3 fs-6">
                                        <p class="m-0 fw-bolder">更多資訊</p>
                                        <p class="m-0 text-black-50">呂亮進 (portaly.cc)</p>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer d-flex ">
                <button type="button" class="btn btn-dark w-100 rounded-pill" data-bs-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
"""
