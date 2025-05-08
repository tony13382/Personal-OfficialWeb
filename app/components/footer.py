class Footer:
    def __str__(self):
        return """
<footer class="bg-theme text-light" style="border-radius: 2rem 2rem 0rem 0rem;">
    <div class="container py-4">
        <div class="row">
            <div class="col-12 col-md-6 col-lg-4 text-decoration-none my-4">
                <h4 class="fs-5">
                    連結 Links
                </h4>
                <a href="https://learn.lianglu.uk/" rel="noopener noreferrer"
                    class="text-decoration-none footer-link">
                    <p class="footer_item">
                        <i class="bi bi-book-half"></i>
                        知識推薦獲取來源
                    </p>
                </a>
                <a href="https://bm.lianglu.uk/" rel="noopener noreferrer"
                    class="text-decoration-none footer-link">
                    <p class="footer_item">
                        <i class="bi bi-bookmark-heart-fill"></i>
                        推薦工作書籤
                    </p>
                </a>
                <a href="https://meowlu.notion.site/ML-12e7c67f7f2d47249f0111882d932663" target="_blank"
                    rel="noopener noreferrer" class="text-decoration-none footer-link">
                    <p class="footer_item">
                        <i class="bi bi-archive-fill"></i>
                        學習資源庫
                    </p>
                </a>
                <a href="https://www.instagram.com/digi.ocean/?hl=zh-tw" target="_blank" rel="noopener noreferrer"
                    class="text-decoration-none footer-link">
                    <p class="footer_item">
                        <i class="bi bi-instagram"></i>
                        旗下知識帳號（DigiOcean）
                    </p>
                </a>
            </div>
            <div class="col-12 col-md-6 col-lg-4 my-4">
                <h4 class="fs-5">
                    贊助 Donate
                </h4>
                <a href="https://www.buymeacoffee.com/liangchinml" target="_blank" rel="noopener noreferrer"
                    class="text-decoration-none footer-link">
                    <p class="footer_item">
                        <i class="bi bi-cup-hot-fill"></i>
                        Buy Me A Coffee
                    </p>
                </a>
                <a href="https://portaly.cc/liang_chin_ml/support" target="_blank" rel="noopener noreferrer"
                    class="text-decoration-none footer-link">
                    <p class="footer_item">
                        <i class="bi bi-cash-stack"></i>
                        贊助系統（Portaly）
                    </p>
                </a>
            </div>
            <div class="col-12 col-md-6 col-lg-4 my-4">
                <h4 class="fs-5">
                    聯絡 Connections
                </h4>
                <a class="text-decoration-none footer-link" href="mailto:liangchinlu@gmail.com" target="_blank">
                    <p class="footer_item">
                        <i class="bi bi-envelope-fill"></i>
                        Email
                    </p>
                </a>
                <a class="text-decoration-none footer-link" href="https://www.instagram.com/liang_chin_ml/"
                    target="_blank">
                    <p class="footer_item">
                        <i class="bi bi-instagram"></i>
                        Instagram
                    </p>
                </a>
                <a class="text-decoration-none footer-link" href="https://www.facebook.com/tony13382/"
                    target="_blank">
                    <p class="footer_item">
                        <i class="bi bi-facebook"></i>
                        Facebook
                    </p>
                </a>
                <a class="text-decoration-none footer-link" href="https://portaly.cc/liang_chin_ml" target="_blank">
                    <p class="footer_item">
                        <i class="bi bi-info-square-fill"></i>
                        Portaly 傳送門
                    </p>
                </a>
            </div>
            <hr>
            <p class="text-lightpink text-center py-2">
                Copyright © 2025 Liang-Chin, Lu 版權所有
            </p>
        </div>
    </div>
</footer>
<!-- Optional JavaScript; choose one of the two! -->

<!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous">
    </script>
<script src="/assets/script/scroll.js"></script>
<script type="text/javascript" src="/assets/script/lozad.min.js"></script>
<script>
    const observer = lozad(); // lazy loads elements with default selector as '.lozad'
    observer.observe();
</script>
"""
